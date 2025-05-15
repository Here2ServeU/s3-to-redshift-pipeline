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

---
## <div align="center">About the Author</div>

<div align="center">
  <img src="assets/emmanuel-naweji.jpg" alt="Emmanuel Naweji" width="120" height="120" style="border-radius: 50%;" />
</div>

**Emmanuel Naweji** is a seasoned Cloud and DevOps Engineer with years of experience helping companies architect and deploy secure, scalable infrastructure. He is the founder of initiatives that train and mentor individuals seeking careers in IT and has helped hundreds transition into Cloud, DevOps, and Infrastructure roles.

- Book a free consultation: [https://here4you.setmore.com](https://here4you.setmore.com)
- Connect on LinkedIn: [https://www.linkedin.com/in/ready2assist/](https://www.linkedin.com/in/ready2assist/)

Let's connect and discuss how I can help you build reliable, automated infrastructure the right way.



--- 

MIT License © 2025 Emmanuel Naweji

You are free to use, copy, modify, merge, publish, distribute, sublicense, or sell copies of this software and its associated documentation files (the “Software”), provided that the copyright and permission notice appears in all copies or substantial portions of the Software.

This Software is provided “as is,” without any warranty — express or implied — including but not limited to merchantability, fitness for a particular purpose, or non-infringement. In no event will the authors be liable for any claim, damages, or other liability arising from the use of the Software.
