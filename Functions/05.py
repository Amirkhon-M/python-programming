"""
Write a program to sum the Fibonacci series up to n (input n). 1, 1, 2, 3, 5, 8, 13, …
"""


def fibonacci_sum(n):
    fib_sequence = [1, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return sum(fib_sequence)


def main():
    n = int(input("Enter the value of n: "))
    result = fibonacci_sum(n)
    print(f"The sum of Fibonacci series up to {n} is: {result}")
    return n


if __name__ == "__main__":
    main()
