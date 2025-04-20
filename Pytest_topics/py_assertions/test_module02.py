import pytest

def test_case01():
    with pytest.raises(Exception):
        assert (1/0)

def func1():
    raise ValueError("Indexerror func1 raised")

def test_case02():
    with pytest.raises(Exception) as excinfo:
        #assert (1,2,3) == (1,2,4)
        func1()
    print(str(excinfo))
    assert(str(excinfo.value)) == 'Exception func1 raised'

