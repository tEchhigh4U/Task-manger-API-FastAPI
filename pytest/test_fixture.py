import pytest
import psycopg2

# test fixture as example data to pass a function
# Define a fixture function
@pytest.fixture
def example_data():
    data = {"name": "John", "age": 20}
    return data

# Use the fixture function in a test function
def test_example_data(example_data):
    assert example_data["name"] == "John"
    assert example_data["age"] == 20


# test database connection
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

def test_database(db_connection):
    # test db_connection
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM flights")
    result = cursor.fetchall()
    assert result is not None