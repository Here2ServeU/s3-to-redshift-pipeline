# S3 to Redshift Log Ingestion Pipeline

This project automates log processing from an S3 bucket to Amazon Redshift using AWS Lambda, SQS, and Python.

## Components

### `lambda/log_processor.py`
Lambda function triggered by S3 upload. It reads a gzipped JSON log file, decompresses it, parses each line, and sends the log data to an SQS queue.

### `lambda.zip`
Packaged version of the Lambda function ready for deployment using Terraform or AWS CLI.

### `terraform/`
Contains infrastructure-as-code configuration to deploy the pipeline. (To be added)

### `scripts/create_redshift_table.sql`
SQL script to create a Redshift table for storing logs. (To be added)

### `event_sample/s3_event.json`
Sample S3 event to test the Lambda function locally or in a simulation. (To be added)

## Usage

1. Deploy the infrastructure using Terraform.
2. Upload gzipped JSON logs to S3.
3. Lambda processes the log, sends entries to SQS.
4. Downstream process ingests from SQS into Redshift.

## Environment Variables

- `SQS_URL`: URL of the target SQS queue.
