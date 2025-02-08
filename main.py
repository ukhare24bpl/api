import boto3

def get_all_databases():
    """Fetch list of databases from AWS Glue."""
    glue_client = boto3.client('glue')
    try:
        response = glue_client.get_databases()
        return [db['Name'] for db in response.get('DatabaseList', [])]
    except Exception as e:
        print(f"Error fetching databases: {e}")
        return []

def get_all_tables(database_name):
    """Fetch list of tables for a given database."""
    glue_client = boto3.client('glue')
    try:
        response = glue_client.get_tables(DatabaseName=database_name)
        return [table['Name'] for table in response.get('TableList', [])]
    except Exception as e:
        print(f"Error fetching tables for database {database_name}: {e}")
        return []

def get_table_details(database_name, table_name):
    """Fetch metadata details for a given table."""
    glue_client = boto3.client('glue')
    try:
        response = glue_client.get_table(DatabaseName=database_name, Name=table_name)
        return response.get('Table', {})
    except Exception as e:
        print(f"Error fetching details for table {table_name}: {e}")
        return {}

def main():
    databases = get_all_databases()
    
    if not databases:
        print("No databases found.")
        return

    for db in databases:
        print(f"\nDatabase: {db}")
        tables = get_all_tables(db)
        
        if not tables:
            print(f"  No tables found in database '{db}'.")
            continue

        for table in tables:
            print(f"  Table: {table}")
            details = get_table_details(db, table)
            
            # Ensure StorageDescriptor exists before accessing 'Columns'
            columns = details.get('StorageDescriptor', {}).get('Columns', [])
            print(f"    Table Schema: {columns}")

if __name__ == "__main__":
    main()
