aws dynamodb delete-table --table-name Metric
aws dynamodb describe-table --table-name Metric
aws dynamodb scan --table-name Metric
aws dynamodb delete-item --table-name Metric --key '{ "id": { "S": "403a74b4-08da-4344-987a-3b149c00d080" } }'