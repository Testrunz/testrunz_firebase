terraform {
  backend "s3" {
    bucket = "testrunz-terraform-be"       # Explicate, cannot use vars, avoid circular deps
    key    = "bootstrap/terraform.tfstate" # changing this key will require a state migration
    region = "us-east-1"
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "3.70.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
variable "aws_region" {
  description = "AWS deployment Region"
  type        = string
  sensitive   = false
}
variable "aws_access_key" {
  type      = string
  sensitive = true
}
variable "aws_secret" {
  type      = string
  sensitive = true
}

variable "aws_account_num" {
  type      = string
  sensitive = true
}

variable "github_project_name" {
  type      = string
  sensitive = false
}
variable "github_access_token" {
  type      = string
  sensitive = true
}

variable "bucket_name" {
  type      = string
  sensitive = false
}

variable "github_source_repo" {
  type      = string
  sensitive = false
}

resource "aws_s3_bucket" "tf_S3_backend" {
  bucket = var.bucket_name
  acl    = "private"

  versioning {
    enabled = true
  }
  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_secretsmanager_secret" "codebuild-tf-secrets" {
  name = "codebuild-tf-secrets"
}

# Build all at once? ECR -> Docker Compose -> Production ECS Deployment

resource "aws_secretsmanager_secret_version" "codebuild-tf-secrets-ver" {
  secret_id = aws_secretsmanager_secret.codebuild-tf-secrets.id
  secret_string = jsonencode({
    github_source_repo : "${var.github_source_repo}",
    github_project_name : "${var.github_project_name}",
    github_access_token : "${var.github_access_token}",
    bucket_name : "${var.bucket_name}",
    aws_access_key : "${var.aws_access_key}",
    aws_secret : "${var.aws_secret}",
    aws_account_num : "${var.aws_account_num}",
    aws_region : "${var.aws_region}",
    client_react_app_api : "",            // api path ex; localhost:5000/api
    client_react_app : "",                // react app uri ex: localhost:5000 & domain.com
    client_port : "",                     // react app container port
    client_skip_preflight_check : "true", // craco related conf
    server_node_env : "",                 // development || production
    server_port : "",                     // server port #
    server_secret : "",                   // salt
    server_client_url : "",               // ??? 
    server_db_connection : ""             // mongo/documentdb
    # server_jwt_secret : "" # Currently commented out in code
  })
}

resource "aws_codebuild_webhook" "terraform-cicd-webhook" {
  project_name = aws_codebuild_project.terraform-cicd.name
  build_type   = "BUILD"
  filter_group {
    filter {
      type    = "EVENT"
      pattern = "PUSH"
    }

    filter {
      type    = "HEAD_REF"
      pattern = "main"
    }
  }
}

resource "aws_codebuild_source_credential" "testrunzghtoken" {
  auth_type   = "PERSONAL_ACCESS_TOKEN"
  server_type = "GITHUB"
  token       = var.github_access_token
}

resource "aws_codebuild_project" "terraform-cicd" {
  name          = "terraform-cicd"
  description   = "terraform deployment codebuild instance"
  build_timeout = "5"
  service_role  = aws_iam_role.codebuild-assume.arn
  badge_enabled = true
  artifacts { # see cloudwatch logs for details
    type = "NO_ARTIFACTS"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/standard:5.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"
  }


  logs_config {
    cloudwatch_logs {
      group_name  = "/aws/codebuild/${var.github_project_name}"
      stream_name = "iac/${var.github_project_name}"
    }
  }

  source {
    type            = "GITHUB"
    location        = var.github_source_repo
    git_clone_depth = 1
    buildspec       = file("./buildspec.yml")
    git_submodules_config {
      fetch_submodules = false
    }
  }
}



resource "aws_iam_role" "codebuild-assume" {
  name = "codebuild-assume"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "codebuild.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
EOF
}


resource "aws_iam_policy" "codebuild-policy" {
  name        = "codebuild-policy"
  description = "Policy to be used by CodeBuild"

  policy = jsonencode({
    "Version" : "2012-10-17",
    "Statement" : [
      {
        "Effect" : "Allow",
        "Action" : [
          "secretsmanager:GetSecretValue",
          "secretsmanager:DescribeSecret",
          "secretsmanager:CreateSecret",
          "secretsmanager:ListSecretVersionIds",
          "secretsmanager:UpdateSecret"
        ],
        "Resource" : "*"
      },
      {
        "Effect" : "Allow",
        "Resource" : [
          "${aws_s3_bucket.tf_S3_backend.arn}",
          "${aws_s3_bucket.tf_S3_backend.arn}/*"
        ],
        "Action" : [
          "s3:ListBucket",
          "s3:GetBucketVersioning",
          "s3:GetObject",
          "s3:PutObject",
          "s3:GetBucketAcl",
          "s3:GetBucketLocation"
        ]
      },
      {
        "Effect" : "Allow",
        "Resource" : [
          "arn:aws:logs:us-east-1:707552785522:log-group:/aws/codebuild/test*",
          "arn:aws:logs:us-east-1:707552785522:log-group:/aws/codebuild/*"
        ],
        "Action" : [
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents"
        ]
      },
      {
        "Effect" : "Allow",
        "Action" : [
          "codebuild:CreateReportGroup",
          "codebuild:CreateReport",
          "codebuild:UpdateReport",
          "codebuild:BatchPutTestCases",
          "codebuild:BatchPutCodeCoverages"
        ],
        "Resource" : [
          "arn:aws:codebuild:us-east-1:${var.aws_account_num}:report-group/*"
        ]
      }
    ]
  })
}

resource "aws_iam_role_policy_attachment" "test-attach" {
  role       = aws_iam_role.codebuild-assume.name
  policy_arn = aws_iam_policy.codebuild-policy.arn
}

# Needs IAM for Codebuild access to TF secrets

# Create Policies

# Build pipeline with access to S3, necessary Secrets in Secret Manager

# Populate buildspec with secrets from secrets.tfvars

# secrets.tfvars -> Secret Manager -> buildspec.yml

# Use cloudwatch logs to debug issues