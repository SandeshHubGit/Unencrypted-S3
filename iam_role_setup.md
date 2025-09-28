# 🔐 Task 2: IAM Role for Lambda (S3 Encryption Monitor)

To allow your Lambda function to inspect S3 bucket encryption settings, we will create an IAM role with read-only access to S3.

---

## ✅ Step-by-Step Instructions

### 1. Open IAM Console

- Navigate to: [AWS IAM Console](https://console.aws.amazon.com/iam/)
- Click **Roles** → **Create role**

---

### 2. Select Trusted Entity

- Choose **AWS Service**
- Use Case: **Lambda**
- Click **Next**

---

### 3. Attach Permissions Policy

Attach the managed AWS policy:

```
AmazonS3ReadOnlyAccess
```

This grants:
- List and describe buckets
- View encryption settings

✅ This is sufficient to detect unencrypted buckets

---

### 4. Name the Role

- Suggested name: `LambdaS3MonitorReadOnlyRole`
- Click **Create role**

---

### 5. Confirm Role

- Go to **Roles** → Find your newly created role
- Ensure `AmazonS3ReadOnlyAccess` is attached

---

✅ Now this role can be assigned to your Lambda function in the next step.