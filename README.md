# 📈 Real-Time Stock Price Monitoring & Analysis

## Project Overview  
This project streams, processes, and stores real-time stock price data using **AWS Kinesis, Apache Flink, Firehose, and S3**.  

## Technologies Used
- AWS Kinesis → Real-time data streaming  
- Apache Flink → Stream processing  
- AWS Firehose → Data delivery  
- Amazon S3 → Transformed data storage  
- Python → Data producer  
- Boto3 → AWS SDK for Python  

---

## Architecture**
The project follows this data pipeline:  

1️⃣ Data Producer** → Python script generates stock price data.  
2️⃣ Data Collection** → AWS Kinesis Data Stream ingests the data.  
3️⃣ Data Processing** → Managed Apache Flink processes real-time data.  
4️⃣ Transformed Storage** → Data is stored in Amazon S3 via Firehose**.  


## 📂 Project Structure:
real-time-stock-monitoring/
│-- data_producer/
│   ├── producer.py        # Generates and sends stock data to Kinesis
│-- flink_processing/
│   ├── flink_job.py       # Processes data with Apache Flink
│-- aws_setup/
│   ├── create_kinesis.sh  # AWS CLI script to create Kinesis stream
│   ├── create_firehose.sh # AWS CLI script to create Firehose delivery stream
│   ├── create_s3.sh       # AWS CLI script to create an S3 bucket
│-- requirements.txt       # Dependencies
│-- README.md              # Project Documentation
