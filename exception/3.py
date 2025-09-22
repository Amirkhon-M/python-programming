# Okay, so how to handle all exceptions?

# Look at the code below:
try:
    number = int(input("Enter a number: "))
    print(1/number)
except ZeroDivisionError:
    print("You can't divide by zero!")
except TypeError:
    print("Data types don't match!")
except ValueError:
    print("Data type must be integer!")
except Exception:
    print("An unxpected error occured and we couldn't find the cause yet :(")
finally:
    print("The application is closing...")

# In this example, we are pinpoiting exact error types, and only when the issue could not be found, we use Exception.