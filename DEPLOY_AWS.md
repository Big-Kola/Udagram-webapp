# Deploy Udagram to AWS with Terraform

## Architecture

```
CloudFront ──── S3 (frontend static files)
    │
    └── /api/* ── ALB ── ECS Fargate (API)
                            │
                            └── RDS PostgreSQL
```

- **Frontend** → S3 bucket + CloudFront CDN
- **API** → ECS Fargate (2 tasks) behind an ALB
- **Database** → RDS PostgreSQL (db.t4g.micro)
- **Networking** → VPC with public/private subnets across 2 AZs

---

## Prerequisites

```bash
# Check all are installed
aws --version          # >= 2.x
terraform --version    # >= 1.5
docker --version       # >= 24
node --version         # >= 18
```

```bash
# Authenticate with AWS
aws configure
# Enter: AWS Access Key ID, Secret Access Key, region (us-east-1)
```

---

## Step 1: Create Terraform State Bucket

Terraform needs an S3 bucket to store its state file.

```bash
aws s3 mb s3://udagram-terraform-state --region us-east-1
aws s3api put-bucket-versioning \
  --bucket udagram-terraform-state \
  --versioning-configuration Status=Enabled
```

---

## Step 2: Configure Variables

```bash
cp terraform/terraform.tfvars.example terraform/terraform.tfvars
```

Edit `terraform/terraform.tfvars` with your values:

```hcl
db_username = "udagram_admin"
db_password = "generate-a-strong-password"
jwt_secret  = "generate-a-random-secret"
```

---

## Step 3: Provision Infrastructure with Terraform

```bash
cd terraform
terraform init
terraform plan
terraform apply -auto-approve
```

After completion, Terraform outputs:

| Output                  | Description                         |
|-------------------------|-------------------------------------|
| `api_url`               | ALB DNS name (e.g. `udagram-...us-east-1.elb.amazonaws.com`) |
| `cloudfront_url`        | CloudFront distribution URL         |
| `ecr_api_repository_url`| ECR repo URL for the API Docker image |
| `rds_endpoint`          | RDS hostname                        |
| `s3_bucket_name`        | S3 bucket for frontend upload       |

Save these outputs for the next steps.

---

## Step 4: Build & Push API Docker Image

```bash
# Authenticate Docker to ECR
aws ecr get-login-password --region us-east-1 \
  | docker login --username AWS --password-stdin \
    $(terraform -chdir=terraform output -raw ecr_api_repository_url | cut -d'/' -f1)

# Build and tag the image
cd udagram-api
docker build -t udagram-api .

ECR_REPO=$(terraform -chdir=../terraform output -raw ecr_api_repository_url)
docker tag udagram-api:latest ${ECR_REPO}:latest
docker push ${ECR_REPO}:latest
cd ..
```

---

## Step 5: Build & Upload Frontend

```bash
# Install dependencies and build
cd udagram-frontend
npm ci
npm run build

# Upload to S3
S3_BUCKET=$(terraform -chdir=../terraform output -raw s3_bucket_name)
aws s3 sync dist/ s3://${S3_BUCKET}/ --delete

# Invalidate CloudFront cache
CF_URL=$(terraform -chdir=../terraform output -raw cloudfront_url)
CF_ID=$(aws cloudfront list-distributions \
  --query "DistributionList.Items[?DomainName=='${CF_URL}'].Id" \
  --output text)
aws cloudfront create-invalidation --distribution-id ${CF_ID} --paths "/*"
cd ..
```

---

## Step 6: Update ECS Service to Use New Image

```bash
# Force ECS to redeploy with the latest image
aws ecs update-service \
  --cluster udagram-prod \
  --service udagram-api \
  --force-new-deployment
```

---

## Step 7: Verify

```bash
# Health check via ALB
API_URL=$(terraform -chdir=terraform output -raw api_url)
curl -s http://${API_URL}/health
# Expected: {"status":"ok"}

# Check the API root
curl -s http://${API_URL}/
# Expected: JSON with endpoints listing

# Through CloudFront
CF_URL=$(terraform -chdir=terraform output -raw cloudfront_url)
curl -s http://${CF_URL}/api/v0/health
# Expected: {"status":"ok"}
```

Open `${CF_URL}` in a browser. You should see the Udagram app.

---

## Step 8: ECS Logs (Troubleshooting)

```bash
aws logs tail /ecs/udagram-api --follow
```

---

## Full Redeploy (One-Liner)

When you make code changes, rebuild and redeploy everything:

```bash
# 1. Build and push API
cd udagram-api && docker build -t udagram-api . && \
  ECR_REPO=$(terraform -chdir=../terraform output -raw ecr_api_repository_url) && \
  docker tag udagram-api:latest ${ECR_REPO}:latest && \
  docker push ${ECR_REPO}:latest && \
  aws ecs update-service --cluster udagram-prod --service udagram-api --force-new-deployment && \
  cd ..

# 2. Build and upload frontend
cd udagram-frontend && npm ci && npm run build && \
  S3_BUCKET=$(terraform -chdir=../terraform output -raw s3_bucket_name) && \
  aws s3 sync dist/ s3://${S3_BUCKET}/ --delete && \
  CF_URL=$(terraform -chdir=../terraform output -raw cloudfront_url) && \
  CF_ID=$(aws cloudfront list-distributions \
    --query "DistributionList.Items[?DomainName=='${CF_URL}'].Id" \
    --output text) && \
  aws cloudfront create-invalidation --distribution-id ${CF_ID} --paths "/*"
```

---

## Clean Up

```bash
cd terraform
terraform destroy -auto-approve
```

> **Note:** The RDS final snapshot will remain after destroy. Delete it manually via the AWS Console if not needed:
> `aws rds delete-db-snapshot --db-snapshot-identifier udagram-prod-final-YYYY-MM-DD-hhmm`

---

## Issues Fixed Before Deployment

| Issue | File | Fix |
|-------|------|-----|
| `force: true` drops DB on restart | `udagram-api/src/index.ts:32` | Only forces sync in dev; production syncs without dropping |
| Hardcoded `localhost:8080` API URL | `udagram-frontend/src/environments/environment.prod.ts` | Uses `window.__env__.apiUrl` with `/api/v0` fallback (same-origin via CloudFront) |
| Hardcoded DB password in sequelize config | `udagram-api/src/migrations/config/config.json` | Replaced with JS config reading env vars |
| CORS wide open | `udagram-api/src/server.ts` | Accepts `CORS_ORIGIN` env var (defaults to `*`) |
| No Dockerfile | `udagram-api/Dockerfile` | Multi-stage build with health checks |
| No infrastructure code | `terraform/` | Full VPC, RDS, ECS, ALB, S3, CloudFront setup |
