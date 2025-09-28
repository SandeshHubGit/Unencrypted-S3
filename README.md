# Unencrypted-S3

## 🔍 Assignment 3: Monitor Unencrypted S3 Buckets Using AWS Lambda & Boto3

This project implements a serverless Lambda function that automatically detects any S3 buckets without server-side encryption enabled. It helps improve your AWS security posture using Boto3 and the AWS SDK for Python.

---

## 📁 Project Structure

```
Assignment_3_Unencrypted_S3_Monitor/
├── 01_s3_setup/             # S3 bucket creation (some encrypted, some not)
├── 02_iam_role/             # IAM role with AmazonS3ReadOnlyAccess
├── 03_lambda_function/      # Lambda function to detect unencrypted buckets
├── 04_documentation/        # Final README
```

---

## ✅ Tasks Overview

### Task 1: S3 Setup

- Create 2–3 S3 buckets
- Enable encryption (SSE-S3 or SSE-KMS) on some
- Leave encryption disabled on at least one bucket

---

### Task 2: IAM Role for Lambda

- Role name: `LambdaS3MonitorReadOnlyRole`
- Attach managed policy: `AmazonS3ReadOnlyAccess`
- This allows Lambda to inspect all buckets

---

### Task 3: Lambda Function

- Runtime: Python 3.x
- IAM Role: `LambdaS3MonitorReadOnlyRole`
- Script: `s3_encryption_monitor.py`

**Function Behavior:**
- Lists all buckets
- Checks if encryption is enabled
- Logs buckets without encryption
- Returns list of unencrypted buckets

---

### Task 4: Manual Invocation

- Open Lambda Console → Choose your function → Click **Test**
- Select default test event and execute
- Observe the logs to see:
  - ✅ Encrypted buckets
  - ❌ Unencrypted buckets
- Returned payload will show list of unencrypted bucket names

---

## 🧪 Validation

- Ensure at least one bucket is detected as unencrypted
- Confirm that the logs show correct encryption detection behavior
- Check that encrypted buckets are not flagged

---
