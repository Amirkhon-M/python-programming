# Now let's see another example with exception handling

try:
    number = int(input("Enter a number: "))
    print(1/number)
except Exception:
    print("An unexpected error occurred.")

# While in this example, the error is catched, it is still not a good practice to catch all exceptions.
# You want to tell users what exactly went wrong and not play a guessing game(like MicroSoft))) ).

# Go to 3.py to see the improved version of this code.