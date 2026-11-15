import psycopg2
import getpass

# Database configuration
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "titanic_db"
DB_USER = "postgres"

# Enter PostgreSQL password
DB_PASSWORD = getpass.getpass("Enter PostgreSQL password: ")

try:
    # Connect to PostgreSQL
    connection = psycopg2.connect(
        host=DB_HOST,
        port=DB_PORT,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )

    print("PostgreSQL connected successfully!")

    # Create cursor
    cursor = connection.cursor()

    # Count passenger records
    cursor.execute("""
        SELECT COUNT(*)
        FROM titanic_project.passengers;
    """)

    result = cursor.fetchone()

    print("Total Titanic passengers:", result[0])

    cursor.close()
    connection.close()

    print("Connection closed successfully!")

except psycopg2.Error as error:
    print("Database connection failed:", error)