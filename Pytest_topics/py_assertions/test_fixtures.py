import pytest
@pytest.fixture()
def setup_list():
    print("/n in fixtures")
    city = ['New york','London','Riyadh','Singapore','Mumbai']
    return city

def test_getItem(setup_list):
    print(setup_list[1:3])
    assert setup_list[0] == 'New york'
    assert setup_list[::2] == ['New york','Riyadh','Mumbai']