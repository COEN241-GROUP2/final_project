aws lambda create-function \
    --function-name coldstart_256m \
    --memory-size 256 \
    --zip-file fileb://function.zip \
    --handler lambda_handler \
    --runtime python3.8 \
    --role arn:aws:iam::111649035132:role/service-role/scalability_test-role-itcuy25d