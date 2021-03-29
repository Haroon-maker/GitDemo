class Calculator:
    num = 100

    def __init__(self, a, b):
        """
        :param a:
        :param b:
        """
        print("I am constructor i will be called automatically then classes object is created")
        self.firstNumber = a
        self.secondNumber = b

    @staticmethod
    def get_data():
        print("We are learning the classes basic")

    def submission(self):
        return self.firstNumber + self.secondNumber + Calculator.num


obj = Calculator(4, 3)   # create an object of a class
obj.get_data()
print(obj.submission())