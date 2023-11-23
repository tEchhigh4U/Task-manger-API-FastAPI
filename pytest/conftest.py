import pytest
import psycopg2

# test fixture as example data to pass a function
@pytest.fixture
def example_data():
    data = {"name": "John", "age": 20}
    return data

@pytest.fixture
def db_connection():
    # connect to the database in the postgres
    conn = psycopg2.connect(
        dbname="self_learn", 
        user="postgres", 
        password="postgres",
        host="localhost"
    )
    yield conn #provide the connected database to the test
    conn.close() # close the connection after the test runs