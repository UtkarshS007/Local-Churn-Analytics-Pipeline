from dagster import job, op
import subprocess

@op
def ingest_data():
    subprocess.run(["python", "C:/Projects/Local-Churn-Analytics-Pipeline/ingestion.py"])
    return "Ingestion of Data Completed."

@op
def transform_data(context, ingestion_status: str):
    context.log.info(ingestion_status)
    subprocess.run(["python", "C:/Projects/Local-Churn-Analytics-Pipeline/featureeng.py"])
    return "Feature Engineering and Transformation Completed."

@op
def train_model(context, transformation_status: str):
    context.log.info(transformation_status)
    subprocess.run(["python", "C:/Projects/Local-Churn-Analytics-Pipeline/ML/train.py"])

@job
def churn_prediction_pipeline():
    ingestion_status = ingest_data()
    transformation_status = transform_data(ingestion_status)
    train_model(transformation_status)
