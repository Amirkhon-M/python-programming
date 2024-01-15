"""
The following list contains some fruits:
fruits = ['banana', 'orange', 'mango', 'lemon']
If a fruit doesn't exist in the list add the fruit to the list and print the modified list. If the fruit exists
 print('That fruit already exist in the list')
"""

def add_fruit_to_list(fruit, fruits):
    if fruit not in fruits:
        fruits.append(fruit)
        print(f"{fruit} is added to the list. Here is a modified list: {fruits}")
    else:
        print(f"That fruit already exists in the list. List remains unchanged: {fruits}")


def main():
    fruits = ['banana', 'orange', 'mango', 'lemon']
    while True:
        fruit_to_add = input("Enter a fruit: ")
        add_fruit_to_list(fruit_to_add, fruits)
        print("Final list:", fruits)


if __name__ == "__main__":
    main()
