import boto3

def get_databases():
    glue_client = boto3.client('glue')

    try:
        response = glue_client.get_databases()
        databases = response.get('DatabaseList', [])
        return [db['Name'] for db in databases]  # Extracting database names
    except Exception as e:
        print(f"Error fetching databases: {e}")
        return []

# Example Usage
databases = get_databases()
print("Databases:", databases)
