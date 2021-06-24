## Translating content dynamically using S3 Object Lambda

The following files are included with this sample

#### DynamicFileTranslation-Lambda.py
This is the Python script for the Lambda function that needs to be created and associated with the S3 Object Lambda Access Point.

#### s3ol_client.py
This is Python script to test dynamic file translations using S3 Object Lambda. Run this scrpit from the command-line and pass the code of the target language.
Before running this script, make sure you replace the value within the '<>' in line 26 with your own S3 Object Lambda access point ARN.
USAGE: 
  s3ol_client.py <Target Language Code>
  e.g. [joe@192.168.1.10 ~]$ s3ol_client.py "fr"

  ## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.

