# devsecops-image-pipeline

A CI/CD pipeline that builds a Docker image and scans with Trivy for any vunerabilities. If it passes the security check, it will push it to Amazon ECR

# how it works:

1. Push code to GitHub 
2. GitHub Actions builds the Docker image
3. Trivy scans the image for HIGH and CRITICAL vunerabilities 
4. If the scan passes, it is pushed to ECR 
5. If the scan fails then nothing is pushed and the pipeline stops




## Challenges and lessons learned


 1. 45 HIGH vulnerabilities on the first scan

**Problem: Trivy reported 45 HIGH findings in the Debian base image.
**Investigation: The report showed every finding was in the OS layer, not my Python dependencies.
**Solution: Filtered unfixable issues with `--ignore-unfixed`, refreshed the base image with `--pull`, and patched the remaining package with `apt-get upgrade`.
**Lesson: Security scanning is about triage, not just detection  
