import pytest

@pytest.fixture(scope="session")
def before_all():
    print("Begin Test Suite")
    yield
    print("End Test Suite")

@pytest.fixture()
def before_each():
    print("Begin Test")
    yield
    print("End Test")

#tests
def test_sum(before_all, before_each):
    assert 1+1 == 2

#tests
def test_sub(before_all, before_each):
    assert 2-1 == 1