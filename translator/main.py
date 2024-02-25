import json
from difflib import get_close_matches
from colorama import Fore, Style


def search(word, data):
    if word in data:
        definition = data[word]
        print(Fore.LIGHTGREEN_EX + f"Definition of '{word}':\n{definition}")
    else:
        suggestions = get_close_matches(word, data.keys())
        if suggestions:
            print(Fore.LIGHTRED_EX + f"No word '{word}' found =(")
            print("Did you mean:")
            for idx, suggestion in enumerate(suggestions, start=1):
                print(Fore.LIGHTGREEN_EX + f"{idx}. {suggestion}")
            choice = input(Fore.LIGHTWHITE_EX + "Enter the number of your choice, or press Enter to exit: ")
            if choice.isdigit() and 1 <= int(choice) <= len(suggestions):
                search(suggestions[int(choice) - 1], data)
        else:
            print(Fore.LIGHTRED_EX + "No suggestions found.")


def main():
    try:
        with open('data.json') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(Fore.LIGHTRED_EX + "Error: 'data.json' file not found.")
        return
    except json.JSONDecodeError:
        print(Fore.LIGHTRED_EX + "Error: 'data.json' file is not valid JSON.")
        return

    while True:
        word = input(Fore.LIGHTWHITE_EX + "Enter a word (or press Enter to exit): ")
        if not word:
            break
        search(word.lower(), data)


if __name__ == "__main__":
    main()
