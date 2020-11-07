# delete table
aws dynamodb delete-table --table-name Metric

# recreate table
python create_table.py

# run tests
artillery run load_test.yaml

