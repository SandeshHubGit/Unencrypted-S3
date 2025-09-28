# 🛡️ Assignment 3: Monitor Unencrypted S3 Buckets with AWS Lambda & Boto3

---

## ✅ Task 1: S3 Bucket Setup for Encryption Monitoring

In this task, we will create S3 buckets — some with encryption enabled and others without — to be scanned by a Lambda function that detects unencrypted buckets.

---

### 📁 Create Sample Buckets

1. Navigate to: [AWS S3 Console](https://s3.console.aws.amazon.com/s3)
2. Click **Create bucket**
3. Create at least **3 buckets** with these variations:

#### Example:
- `encrypted-bucket-001` ✅ Server-side encryption (SSE-S3 or SSE-KMS)
- `unencrypted-bucket-001` ❌ No encryption
- `encrypted-bucket-002` ✅ Server-side encryption (SSE-S3)

---

### 🔐 Enable Encryption for Some Buckets

- During bucket creation or after, go to:
  - **Properties → Default encryption**
- Enable **SSE-S3** or **SSE-KMS**
- For others, **leave encryption OFF**

---

### 🧪 Testing Requirements

- At least **1 bucket without encryption** must exist.
- At least **1 or more buckets with encryption** enabled for verification.

---

✅ Once this is done, proceed to creating the IAM role with `AmazonS3ReadOnlyAccess` for Lambda.