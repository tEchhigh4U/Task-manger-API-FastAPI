import pytest

# test fixture as example data to pass a function
@pytest.fixture
def example_data():
    data = {"name": "John", "age": 20}
    return data

@pytest.fixture
def db_config():
    # database configuration
    db_config= {
        'dbname':'self_learn', 
        'user':'postgres', 
        'password': 'postgres',
        'host':'localhost',
    }
    return db_config
