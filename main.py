"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Petra Peřinová
email: perinova.petra@seznam.com
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

username = input("username:").lower()
password = input("password:")

line = "-" * 35
print(line)

if username in users and users[username] == password:
    print(f"Welcome to the app, {username}!")
else:
    print ("unregistered user, terminating the program..")
    exit()

print("We have 3 texts to be analyzed.")
print(line)

choice = input("Enter a number btw. 1 and 3: ")
if not choice.isdigit() or int(choice) not in range(1, 4):  
    print("Invalid choice, terminating the program...")
    exit()

text = TEXTS[int(choice) - 1]
#print(f"Selected text:\n{text}")

words = text.split()
count_of_words = len(words)
print(f"There are", count_of_words, "words in the selected text."  )

titlecase_words = [word for word in words if word.istitle()]
count_of_titlecase_words = len(titlecase_words)
print(f"There are", count_of_titlecase_words, "titlecase words.")

uppercase_words = [word for word in words if word.isupper()]
count_of_uppercase_words = len(uppercase_words)
print(f"There are", count_of_uppercase_words, "uppercase words.")

lowercase_words = [word for word in words if word.islower()]
count_of_lowercase_words = len(lowercase_words)
print(f"There are", count_of_lowercase_words, "lowercase words.") 

numeric_strings = [word for word in words if word.isdigit()]
count_of_numeric = len(numeric_strings)
print(f"There are", count_of_numeric, "numeric strings")

print(line)

print("LEN|", "", "OCCURENCES", "", "|NR.")

print (line)

word_lengths = [len(word) for word in words]
length_counts = {}
for length in word_lengths:
    if length in length_counts:
        length_counts[length] += 1
    else:
        length_counts[length] = 1

for length, count in sorted(length_counts.items()):
    print(f"{length:<5} | {'*' * count:<17} | {count:>2}")




