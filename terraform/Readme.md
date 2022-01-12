# Bootstrap

This Repo creates the Terraform Backend bucket, and the CI/CD pipeline used to manage infrastructure.

![CodeBuildBadge](https://codebuild.us-east-1.amazonaws.com/badges?uuid=eyJlbmNyeXB0ZWREYXRhIjoicStBQ0xsRGlwb3EzZ090eGF2RVFnVlRWcGZWblVJUHNlUUJSMzEycTZwQzA4WW1UbW1QNDhweDJoNjZxSzBFRWRLcElyNDdUTitub2tCaXNSeGNCMlRRPSIsIml2UGFyYW1ldGVyU3BlYyI6IklXWG1acDdrZHROVnZYOFIiLCJtYXRlcmlhbFNldFNlcmlhbCI6MX0%3D&branch=main)

## Secrets Needed

> create secret terraform vars file file

``` bash
touch secrets.tfvars
```

| Secrets in secrets.tfvars file | example |
|---|---|
| aws_region | "us-east-1" |
| github_source_repo | "" |
| github_project_name | "" |
| github_access_token | "ghp_XXXXXXDXXX" |
| bucket_name | "testrunz-terraform-be" |
| aws_access_key | "AKIAXXXX" |
| aws_secret | "BxtQasXXXXX" |
| aws_account_num | "70755XXXXXX" |

### Run with

``` bash
terraform apply --var-file="secrets.tfvars"
```
