# Implicit Type Casting

x = .5
y = 2

print(x + y) # x is converted to float without any user involvement
# This is happens when values have different types

print(int(x + y)) # however, we can also explicitly convert the result to int