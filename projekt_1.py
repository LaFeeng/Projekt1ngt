"""
projekt_2.py: první projekt do Engeto Online Python Akademie
author: Daniel Šadibol
email: sadibol.daniel@gmail.com
discord: dzonsnou. 512617534952833034
"""

import re
from collections import Counter

# Seznam registrovaných uživatelů a jejich hesel
users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

# Texty k analýze
TEXTS = [
    '''Situated about 10 miles west of Kemmerer, Fossil Butte is a ruggedly impressive topographic feature that rises sharply some 1000 feet above Twin Creek Valley to an elevation of more than 7500 feet above sea level. The butte is located just north of US 30N and the Union Pacific Railroad, which traverse the valley.''',
    '''At the base of Fossil Butte are the bright red, purple, yellow and gray beds of the Wasatch Formation. Eroded portions of these horizontal beds slope gradually upward from the valley floor and steepen abruptly. Overlying them and extending to the top of the butte are the much steeper buff-to-white beds of the Green River Formation, which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects a portion of the largest deposit of freshwater fish fossils in the world. The richest fossil fish deposits are found in multiple limestone layers, which lie some 100 feet below the top of the butte. The fossils represent several varieties of perch, as well as other freshwater genera and herring similar to those in modern oceans. Other fish such as paddlefish, garpike and stingray are also present.'''
]

# Autentizace uživatele
username = input("Username: ")
password = input("Password: ")

if users.get(username) == password:
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
else:
    print("Unregistered user, terminating the program..")
    exit()

# Výběr textu
while True:
    try:
        choice = int(input("Enter a number between 1 and 3 to select: ")) - 1
        if choice in range(3):
            break
        else:
            print("Please enter a number between 1 and 3.")
    except ValueError:
        print("Invalid input, please enter a number between 1 and 3.")

text = TEXTS[choice]
words = text.split()
titlecase_words = sum(1 for word in words if word.istitle())
uppercase_words = sum(1 for word in words if word.isupper() and not word.isdigit())
lowercase_words = sum(1 for word in words if word.islower())
numeric_strings = sum(1 for word in words if word.isdigit())
numbers = [int(word) for word in words if word.isdigit()]
sum_numbers = sum(numbers)

# Statistiky
print(f"There are {len(words)} words in the selected text.")
print(f"There are {titlecase_words} titlecase words.")
print(f"There are {uppercase_words} uppercase words.")
print(f"There are {lowercase_words} lowercase words.")
print(f"There are {numeric_strings} numeric strings.")
print(f"The sum of all the numbers {sum_numbers}")

# Délky slov
lengths = [len(word.strip(",.")) for word in words]
length_counts = Counter(lengths)

# Graf
print("LEN| OCCURRENCES |NR.")
for length, count in sorted(length_counts.items()):
    print(f"{length:3}|{'*' * count:12} |{count}")
