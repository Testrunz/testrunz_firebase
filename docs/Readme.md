# Howdy, docs need work

## Secret Managment

Environment Variables should be automatically generated, stored, and retrieved from aws_secrets_manager on build by codebuild

|Secret Mangment| |
|---|---|
| local development secrets | .sample.env |
| development secrets | `aws_secretsmanager_secret.codebuild-development.id` |
| qa secrets | `aws_secretsmanager_secret.codebuild-qa.id` |
| produciton secrets | `aws_secretsmanager_secret.codebuild-production.id` |

## Publishing Containers to AWS ECR

## Docker Compose with AWS ECS docker daemon

[Docs](https://docs.docker.com/cloud/ecs-integration/)

[Sample Deployment](https://aws.amazon.com/blogs/containers/deploy-applications-on-amazon-ecs-using-docker-compose/)