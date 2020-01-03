aws lambda create-function --endpoint http://localhost:4574 \
--function-name S3TriggeredLambda \
--zip-file fileb://function.py.zip \
--handler function.lambda_handler \
--runtime python3.6 \
--role arn:aws:iam::12356:role/AWSLambdaBasicExecution

aws lambda --endpoint-url=http://localhost:4574 invoke --function-name S3TriggeredLambda out --log-type Tail \
--query 'LogResult' --output text | base64 -D

aws cloudformation create-stack \
  --template-body file://template.yaml \
  --stack-name cfn-test \
  --parameters ParameterKey=BucketPrefix,ParameterValue=demo-bucket \
  --endpoint-url=http://localhost:4581