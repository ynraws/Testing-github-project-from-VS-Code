# GCP Migration — Banking Microservices (Demo)

**Project:** Legacy On-Prem Banking App Migration to GCP  
**Stack:** Python (FastAPI), Docker, Cloud Run, Cloud SQL (MySQL), Pub/Sub, Terraform, Cloud Build (CI/CD)

This repository contains a complete demo showing how to migrate a simple on-prem monolith to a cloud-native microservices architecture on GCP.

**What you will find**
- 3 microservices: `accounts-service`, `payments-service`, `auth-service` (FastAPI)
- Dockerfiles and Cloud Build YAMLs for each service
- Terraform modules to provision Cloud SQL, Cloud Run, Pub/Sub, Artifact Registry and basic networking
- Migration scripts and sample SQL export
- A sample `architecture-diagram.png` placeholder

> Before deploying: replace placeholders like `<PROJECT_ID>`, `<REGION>`, and `<CLOUDSQL_CONNECTION_NAME>` with your real values.

## Repo layout
```
gcp-migration-banking/
├── microservices/
│   ├── accounts-service/
│   ├── payments-service/
│   └── auth-service/
├── terraform/
├── migration/
└── README.md
```

## Quick local run (each service)
1. `cd microservices/accounts-service`
2. `pip install -r requirements.txt`
3. `uvicorn main:app --reload --port 8080`

## Notes
- This repo is educational and uses placeholders for secrets and connection strings.
- For production, use Secret Manager, private VPC connectors, and strong IAM roles.

