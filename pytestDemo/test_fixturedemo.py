import pytest


@pytest.mark.usefixtures("setup")
class TestExample:

    def test_fixtureDemo1(self):
        print("I will execute in fixture demo1")

    def test_fixtureDemo2(self):
        print("I will execute in fixture demo2")

    def test_fixtureDemo3(self):
        print("I will execute in fixture demo3")

    def test_fixtureDemo4(self):
        print("I will execute in fixture demo4")