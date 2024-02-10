"""
Create a menu driven application to add/update/delete a student information (name, age, school). Input should be asked
 from a user. Everytime after I perform any action, redirect me to the main page.

How to update/delete a correct user? So, after I create a user, application should return the STUDENT ID,
and using that ID I can update/delete necessary to me student.

I have to have an ability to view all students INFO.

Student ID, Student name, Student Age, School
"""

import id_generator
import time
import os
from colorama import Fore

if os.path.exists("db.txt"):
    file = open("db.txt", "r")
else:
    print("The database does not exist")
    exit()

def print_info():
    print(Fore.LIGHTYELLOW_EX + "\n***All Students Info***\n")
    with open("db.txt", "r") as data:
        print(data.read() + "\n")

def add_student():
    print(Fore.LIGHTYELLOW_EX + "\n***Add a New Student***\n")
    name = input(Fore.LIGHTWHITE_EX + "Enter the name: ")
    age = input("Enter the age: ")
    while not age.isdigit() or not 7 <= int(age) <= 18:
        age = input("Enter a valid age (7-18): ")
    grade = input("Enter the grade (1-11): ")
    while not grade.isdigit() or not 1 <= int(grade) <= 11:
        grade = input("Enter a valid grade (1-11): ")

    new_id = id_generator.uuid
    with open("db.txt", "a") as file:
        file.write(f"Name: {name}, Age: {age}, Grade: {grade}, ID: {new_id}\n")
    print("\nStudent Added Successfully\n")

def update_info():
    print(Fore.LIGHTYELLOW_EX + "\n***Update Student's Info***\n")
    search_id = input("Enter Student ID to update: ")
    updated_info = []
    with open("db.txt", "r") as file:
        lines = file.readlines()
        found = False
        for line in lines:
            if f"ID: {search_id}" in line:
                found = True
                print("Student found. Enter updated information:")
                name = input("Enter the name: ")
                age = input("Enter the age: ")
                while not age.isdigit() or not 7 <= int(age) <= 18:
                    age = input("Enter a valid age (7-18): ")
                grade = input("Enter the grade (1-11): ")
                while not grade.isdigit() or not 1 <= int(grade) <= 11:
                    grade = input("Enter a valid grade (1-11): ")
                updated_info.append(f"Name: {name}, Age: {age}, Grade: {grade}, ID: {search_id}\n")
            else:
                updated_info.append(line)
    if not found:
        print("\nStudent not found.\n")
        return
    with open("db.txt", "w") as file:
        file.writelines(updated_info)
    print("\nStudent information updated successfully.\n")

def remove_student():
    print(Fore.LIGHTYELLOW_EX + "\n***Remove a Student***\n")
    search_id = input("Enter Student ID to remove: ")
    with open("db.txt", "r") as file:
        lines = file.readlines()
    with open("db.txt", "w") as file:
        removed = False
        for line in lines:
            if f"ID: {search_id}" not in line:
                file.write(line)
            else:
                removed = True
    if removed:
        print("\nStudent removed successfully.\n")
    else:
        print("\nStudent not found.\n")

def main():
    while True:
        text = (
            "Student Info App\n"
            "1. View all students\n"
            "2. Add a new student\n"
            "3. Update a student's info\n"
            "4. Remove a student\n"
            "0. Exit"
        )
        print(Fore.LIGHTWHITE_EX + text)
        try:
            option = int(input(Fore.LIGHTGREEN_EX + "Option: "))
            if option == 0:
                print(Fore.CYAN + "\nExiting...\n")
                time.sleep(1)
                exit()
            elif option == 1:
                print_info()
            elif option == 2:
                add_student()
            elif option == 3:
                update_info()
            elif option == 4:
                remove_student()
            else:
                print(Fore.RED + "\nInvalid Input!\n")
        except ValueError:
            print(Fore.RED + "\nInvalid Input! Please enter a number.\n")

if __name__ == "__main__":
    main()
