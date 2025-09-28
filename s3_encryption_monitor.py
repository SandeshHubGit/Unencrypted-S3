import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    unencrypted_buckets = []

    try:
        response = s3.list_buckets()

        for bucket in response.get('Buckets', []):
            bucket_name = bucket['Name']
            try:
                enc = s3.get_bucket_encryption(Bucket=bucket_name)
                rules = enc['ServerSideEncryptionConfiguration']['Rules']
                print(f"✅ Bucket '{bucket_name}' has encryption enabled: {rules}")
            except s3.exceptions.ClientError as e:
                error_code = e.response['Error'].get('Code')
                if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                    print(f"❌ Bucket '{bucket_name}' does NOT have encryption enabled.")
                    unencrypted_buckets.append(bucket_name)
                else:
                    print(f"⚠️ Error checking bucket '{bucket_name}': {e}")
    except Exception as e:
        print(f"Unexpected error listing buckets: {e}")

    return {
        'unencrypted_buckets': unencrypted_buckets,
        'count': len(unencrypted_buckets)
    }