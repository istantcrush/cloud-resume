# Cloud Resume Challenge — Andrew He

A serverless cloud resume built on AWS, featuring a live visitor counter and automated CI/CD deployment pipeline.

**Live site:** https://d1wavzvvdzqdgr.cloudfront.net

## Architecture

This project implements a full serverless architecture:

- **Frontend:** Static HTML/CSS hosted on S3, delivered globally via CloudFront CDN over HTTPS
- **Visitor Counter:** JavaScript fetch call → API Gateway → Lambda (Python) → DynamoDB
- **CI/CD:** GitHub Actions automatically deploys to S3 on every push to main
- **Infrastructure as Code:** All AWS resources provisioned via Terraform

## AWS Services Used

| Service | Purpose |
|---|---|
| S3 | Static website hosting |
| CloudFront | CDN, HTTPS, global distribution |
| API Gateway | REST API endpoint |
| Lambda | Serverless compute (Python 3.14) |
| DynamoDB | Visitor count storage (NoSQL) |
| IAM | Least privilege access control |
| CloudWatch | Lambda logging and monitoring |

## Cost Optimization

This architecture costs near zero at resume-scale traffic:
- Lambda: ~$0.000001 per visit (vs $15-30/month for EC2)
- DynamoDB: Free tier covers millions of requests/month
- S3 + CloudFront: Free tier for typical resume traffic

## Infrastructure as Code

All AWS infrastructure is defined in `terraform/main.tf` and can be reproduced with:

```bash