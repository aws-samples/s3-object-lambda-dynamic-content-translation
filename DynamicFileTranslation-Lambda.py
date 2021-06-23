import json
import boto3
from urllib.parse import urlparse, unquote
from pathlib import Path

def lambda_handler(event, context):
    # TODO implement

    print(event) 
 
    object_context = event["getObjectContext"]
    request_route = object_context["outputRoute"]
    request_token = object_context["outputToken"]
    user_request_url = event["userRequest"]["url"]
    supporting_access_point_arn = event["configuration"]["supportingAccessPointArn"]

    print("USER REQUEST URL: ", user_request_url)
   
   # The S3 object key can be found after the Host name in the user request URL
   # The user request URL looks something like this, 
   # "https://<User Request Host>/LegalDisclaimer/disclaimer.txt#de"
   # The target language code passed in the S3 GET request is after the "#" character  
    
    user_request_url = unquote(user_request_url)
    result = user_request_url.split("#")
    user_request_url = result[0]
    targetLang = result[1]
    
   # Extract the S3 Object Key from the user requested URL
    s3Key = str(Path(urlparse(user_request_url).path).relative_to('/'))
       
   # Get the original object from S3
    s3 = boto3.resource('s3')
    
   # To get the original object from S3,use the supporting_access_point_arn 
    s3Obj = s3.Object(supporting_access_point_arn, s3Key).get()
    srcText = s3Obj['Body'].read()
    srcText = srcText.decode('utf-8')

   # Translation original text
    translateClient = boto3.client('translate')
    response = translateClient.translate_text(
                                                Text = srcText,
                                                SourceLanguageCode='en',
                                                TargetLanguageCode=targetLang
                                            )
    
    # Write object back to S3 Object Lambda
    s3client = boto3.client('s3')
    s3client.write_get_object_response(
                                        Body=response['TranslatedText'],
                                        RequestRoute=request_route,
                                        RequestToken=request_token )
    
    return { 'statusCode': 200 }
