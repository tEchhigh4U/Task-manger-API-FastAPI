import pytest
import psycopg2

from conftest import db_config

def get_db_connection(db_config):
    try:
        conn = psycopg2.connect(
            dbname = db_config['dbname'],
            user = db_config['user'],
            password = db_config['password'],
            host = db_config['host'],
        )
        return conn
    except psycopg2.OperationalError as e:
        print(f"Error occurred while connecting to the database: {e}")
        raise e

def test_db_connection(db_config):  #-> The test will fail if the connection attempt is successful
    with pytest.raises(psycopg2.OperationalError):
        # Call the function that should raise an OperationalError
        get_db_connection(db_config)