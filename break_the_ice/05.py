"""
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""


class MyClass:
    def __init__(self):
        self.s = "undefined"

    def set_string(self):
        self.s = input("Enter a string: ")

    def show_string(self):
        return self.s


def test_class_methods():
    my_instance = MyClass()
    my_instance.set_string()
    result = my_instance.show_string()
    print("String entered:", result)


if __name__ == "__main__":
    test_class_methods()
