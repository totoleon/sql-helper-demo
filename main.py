from sqlalchemy import create_engine
from sqlalchemy.sql import text
import os

# Fetch database connection details from environment variables
host = os.getenv('DB_HOST')
dbname = os.getenv('DB_NAME')
user = os.getenv('DB_USER')
password = os.getenv('DB_PASSWORD')

db_url = os.getenv('DATABASE_URL', f'postgresql://{user}:{password}@{host}/{dbname}')

engine = create_engine(db_url)

def run_query(sql_text):
    output = ""
    with engine.connect() as connection:
        result = connection.execute(text(sql_text))
    for row in result:
        output += str(row)
    return output
