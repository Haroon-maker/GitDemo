import pytest


def test_firstProgram():
    msg = "Haroon"
    assert msg == "Hi", "Test failed because strings do not match"


@pytest.mark.skip
def test_secondCreditCard():
    a = 4
    b = 6
    assert a+2 == 6, "Adding do not match"