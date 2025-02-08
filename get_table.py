import boto3

def get_tables(database_name):
    glue_client = boto3.client('glue')
    tables = []
    next_token = None

    try:
        while True:
            # Fetch tables with pagination
            response = glue_client.get_tables(DatabaseName=database_name, NextToken=next_token) if next_token else glue_client.get_tables(DatabaseName=database_name)

            # Extract table names
            tables.extend([table['Name'] for table in response.get('TableList', [])])

            # Check if there's more data
            next_token = response.get('NextToken')
            if not next_token:
                break

        return tables
    except glue_client.exceptions.EntityNotFoundException:
        print(f"Error: Database '{database_name}' not found.")
        return []
    except glue_client.exceptions.AccessDeniedException:
        print("Error: Access Denied! Check IAM permissions.")
        return []
    except glue_client.exceptions.InvalidInputException:
        print("Error: Invalid input. Check database name formatting.")
        return []
    except Exception as e:
        print(f"Unexpected error fetching tables for database {database_name}: {e}")
        return []

# Example Usage
databases = ["your-database-name"]  # Replace with actual database list

if databases:
    tables = get_tables(databases[0])  # Fetch tables from the first database
    if tables:
        print(f"Tables in {databases[0]}:", tables)
    else:
        print(f"No tables found in database '{databases[0]}'.")
else:
    print("No databases available.")

