from dagster import job, op
import subprocess

@op
def ingest_data():
    subprocess.run(["python", "C:\Projects\Local-Churn-Analytics-Pipeline\ingestion.py"])

@op
def transform_data():
    subprocess.run(["python", "C:\Projects\Local-Churn-Analytics-Pipeline\featureeng.py"])

@op
def train_model():
    subprocess.run(["python", "C:\Projects\Local-Churn-Analytics-Pipeline\ML\train.py"])

@job
def churn_prediction_pipeline():
    transform_data(ingest_data())
    train_model(transform_data())
