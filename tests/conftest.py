import pytest

@pytest.fixture()
def set_up():
    print("START TEST")
    yield
    print("FINISH TEST")

@pytest.fixture(scope="module")
def set_group():
    print("ENTER SYSTEM")
    yield
    print("EXIT SYSTEM")

@pytest.fixture()
def auth():
    print("Start authorization")
    yield
    print("Finish authorization")