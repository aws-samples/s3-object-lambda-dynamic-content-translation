## Translating content dynamically by using Amazon S3 Object Lambda

The recent launch of Amazon S3 Object Lambda creates many possibilities to transform data in S3 buckets dynamically. S3 Object Lambda can be used with other AWS serverless services to transform content stored in S3 in many creative ways. One example is using S3 Object Lambda with Amazon Translate to translate and serve content from S3 buckets on demand. 

Using S3 Object Lambda with Amazon Translate, you do not need to translate content in advance for all possible permutations of source to target languages. Instead, you can transform content in near-real time using a data driven model. This can serve multiple language-specific applications simultaneously. 

The files included in this sample can be used to build a simple data driven application to dynamically translate content from a source language to a target language using S3 Object Lambda

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

