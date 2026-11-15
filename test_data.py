import psycopg2
import pandas as pd
import getpass

# Database configuration
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "database": "titanic_db",
    "user": "postgres"
}

# Get password securely
password = getpass.getpass("Enter PostgreSQL password: ")

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        **DB_CONFIG,
        password=password
    )

    print("Database connected successfully!")

    # Retrieve Titanic data
    query = """
        SELECT *
        FROM titanic_project.passengers
        ORDER BY passengerid;
    """

    # Execute query
    cursor = connection.cursor()
    cursor.execute(query)

    # Get column names
    columns = [desc[0] for desc in cursor.description]

    # Retrieve records
    records = cursor.fetchall()

    # Convert records into Pandas DataFrame
    df = pd.DataFrame(records, columns=columns)

    # Display results
    print("\nTitanic Dataset:")
    print(df.head(10))

    print("\nDataset Information:")
    print("Total Rows:", df.shape[0])
    print("Total Columns:", df.shape[1])

    cursor.close()
    connection.close()

    print("\nDatabase connection closed!")

except Exception as error:
    print("Error:", error)