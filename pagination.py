import boto3
def get_all_databases():
    glue_client = boto3.client('glue')
    databases = []
    next_token = None

    while True:
        response = glue_client.get_databases(NextToken=next_token) if next_token else glue_client.get_databases()
        databases.extend([db['Name'] for db in response.get('DatabaseList', [])])
        next_token = response.get('NextToken')
        if not next_token:
            break
    
    return databases

def get_all_tables(database_name):
    glue_client = boto3.client('glue')
    tables = []
    next_token = None

    while True:
        response = glue_client.get_tables(DatabaseName=database_name, NextToken=next_token) if next_token else glue_client.get_tables(DatabaseName=database_name)
        tables.extend([table['Name'] for table in response.get('TableList', [])])
        next_token = response.get('NextToken')
        if not next_token:
            break

    return tables
