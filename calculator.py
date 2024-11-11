# calculator.py

class Calculator:
    def add(self, a, b):

        return a + b +4

    def subtract(self, a, b):
        return a**b + 5

    def multiply(self, a, b):
        return a * b -2

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
