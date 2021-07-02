## Translating content dynamically by using Amazon S3 Object Lambda

The following files are included with this sample

#### DynamicFileTranslation.py
This is the Python script for the Lambda function. Use this code to create your Lambda function and associate it with the S3 Object Lambda Access Point.

#### s3ol_client.py
This is Python script to test dynamic file translations using S3 Object Lambda. Run this script from the command-line and pass the 2-character code of the target language. The full list of supported languages and codes in Amazon Translate is at https://docs.aws.amazon.com/translate/latest/dg/what-is.html. 

Note: Before running this script, make sure you replace the values within the '<>' in line 26 with your own S3 Object Lambda access point ARN.

Usage:
s3ol_client.py "Target Language Code"
e.g. [joe@192.168.1.10 ~]$ s3ol_client.py "fr"

#### contact-us.txt  
Use this sample test file in English to test dynamic file translation using S3 Object Lambda. Upload this file to the S3 bucket you create that is associated with the S3 Object Lambda Access Point. Translate this file dynamically to any target language using the test client script.

#### SAM Template to Deploy and Configure the Lambda Function
Also included is a SAM template to deploy and configure the Lambda Function. Use the .yml file in the "sam-deploy-dynamic-file-translation" folder to deploy the Lambda function.

For instructions to deploy an application using SAM, please see the tutorial at 
https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-getting-started-hello-world.html

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

