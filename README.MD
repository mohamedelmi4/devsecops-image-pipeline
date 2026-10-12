# devsecops-image-pipeline

A CI/CD pipeline that builds a Docker image and scans with Trivy for any vunerabilities. If it passes the security check, it will push it to Amazon ECR

# how it works:

1. Push code to GitHub 
2. GitHub Actions builds the Docker image
3. Trivy scans the image for HIGH and CRITICAL vunerabilities 
4. If the scan passes, it is pushed to ECR 
5. If the scan fails then nothing is pushed and the pipeline stops  
