import json
import boto3
import sys, getopt
  
def main(argv):
	
  try:	
    targetLang = sys.argv[1]
    print("TargetLang = ", targetLang)

    s3 = boto3.client('s3')
    s3Bucket = "my-s3ol-bucket"
    s3Key = "ContactUs/contact-us.txt"

    # Call get_object using the S3 bucket name

    response = s3.get_object(Bucket=s3Bucket,Key=s3Key)
    print("Original Content......\n")
    print(response['Body'].read().decode('utf-8'))

    print("\n")

    # Call get_object using the S3 Object Lambda access point ARN.
    # Replace the value within the <> with your S3 Object Lambda access point ARN

    s3Bucket = <arn:aws:s3-object-lambda:us-west-2:XXXXXXXX:accesspoint/my-s3ol-access-point">
    s3Key = "ContactUs/contact-us.txt#" + targetLang
    response = s3.get_object(Bucket=s3Bucket,Key=s3Key)
    print("Transformed Content......\n")
    print(response['Body'].read().decode('utf-8'))

    return {'Success':200}             
  except:
    print("\n\nUsage: s3ol_client.py <Target Language Code>")

#********** Program Entry Point ***********
if __name__ == '__main__':
    main(sys.argv[1: ])
 