import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello Haroon")


@pytest.mark.xfail
def test_secondCreditCard():
    print("Good morning")


def test_crossBrowser(crossBrowser):
    print(crossBrowser[1])