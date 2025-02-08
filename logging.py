import logging
import boto3

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

def get_databases():
    glue_client = boto3.client('glue')

    try:
        response = glue_client.get_databases()
        databases = response.get('DatabaseList', [])
        logging.info(f"Fetched {len(databases)} databases.")
        return [db['Name'] for db in databases]
    except Exception as e:
        logging.error(f"Error fetching databases: {e}")
        return []
