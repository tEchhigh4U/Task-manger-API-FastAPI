# Use the fixture function in a test function
def test_example_data(example_data):
    assert example_data["name"] == "John"
    assert example_data["age"] == 20

# test database connection
def test_database(db_connection):
    # test db_connection
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM flights")
    result = cursor.fetchall()
    assert result is not None