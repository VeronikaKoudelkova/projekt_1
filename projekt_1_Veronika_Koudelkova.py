"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Koudelkova
email: koudelkova.veronika87@gmail.com
discord: Veronika K.#4490
"""
TEXTS = {
    "a": """Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.""",
    "aa": """At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.""",
    "aaa": """The monument contains 8198 acres and protects
        a portion of the largest deposit of freshwater fish
        fossils in the world. The richest fossil fish deposits
        are found in multiple limestone layers, which lie some
        100 feet below the top of the butte. The fossils
        represent several varieties of perch, as well as
        other freshwater genera and herring similar to those
        in modern oceans. Other fish such as paddlefish,
        garpike and stingray are also present."""
}

registered_users = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123" }


print("username:")
jmeno = input()
print("password:")
heslo = input()


if jmeno in registered_users and heslo in registered_users.values():
    print(f"""Welcome to the app, {jmeno}.\nWe have 3 texts to be analyzed.""")
    print("Enter a number btw. 1 and 3 to select:")
    number_of_text = int(input())
    if number_of_text in range(1, 4):

        list_of_words = list()
        oddelovac = "-" * 50
        print(oddelovac)

        if number_of_text == 1:

            cutted_words = TEXTS["a"].replace(",","").replace(".","")
            list_from_TEXTS_1 = cutted_words.split()

            for word in list_from_TEXTS_1:
                list_of_words.append(word)
            print(f"""There are {len(list_of_words)} words in the selected text.""")

            for word in list_from_TEXTS_1:
                list_of_words.append(word.istitle())
                titlecase_words = list_of_words.count(True)
            print(f"""There are {titlecase_words} titlecase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_1:
                if word.isalpha():
                    list_of_words.append(word.isupper())
                    uppercase_words = list_of_words.count(True)
            print(f"""There are {uppercase_words} uppercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_1:
                if word.isalpha():
                    list_of_words.append(word.islower())
                    lowercase_words = list_of_words.count(True)
            print(f"""There are {lowercase_words} lowercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_1:
                if word.isnumeric():
                    list_of_words.append(word)
                    numeric_strings = len(list_of_words)
            print(f"""There are {numeric_strings} numeric strings.""")
            list_of_words.clear()

            for word in list_from_TEXTS_1:
                if word.isnumeric():
                    list_of_words.append(int(word))
            print(f"""The sum of all the numbers {sum(list_of_words)}.""")
            list_of_words.clear()

            print(oddelovac)

            occurences = {}

            for word in list_from_TEXTS_1:
                length_of_word = len(word)
                if length_of_word not in occurences:
                    occurences[length_of_word] = 1
                else:
                    occurences[length_of_word] += 1

            print(
                oddelovac,
                f"   LEN|   OCCURENCES  |NR.   ",
                oddelovac,
                sep="\n"
                )
            
            for index, occurence in sorted(occurences.items()):
                string = str(index)
                print(f"""{" " * 3}{string.rjust(3)}|{occurence * "*"}{" " * (15 - len(occurence * "*"))}|{occurence}""")

        elif number_of_text == 2:

            cutted_words = TEXTS["aa"].replace(",","").replace(".","")
            list_from_TEXTS_2 = cutted_words.split()

            for word in list_from_TEXTS_2:
                list_of_words.append(word)
            print(f"""There are {len(list_of_words)} words in the selected text.""")
            
            for word in list_from_TEXTS_2:
                list_of_words.append(word.istitle())
                titlecase_words = list_of_words.count(True)
            print(f"""There are {titlecase_words} titlecase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_2:
                if word.isalpha():
                    list_of_words.append(word.isupper())
                    uppercase_words = list_of_words.count(True)
            print(f"""There are {uppercase_words} uppercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_2:
                if word.isalpha():
                    list_of_words.append(word.islower())
                    lowercase_words = list_of_words.count(True)
            print(f"""There are {lowercase_words} lowercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_2:
                if word.isnumeric():
                    list_of_words.append(word)
                    numeric_strings = len(list_of_words)
            print(f"""There are {numeric_strings} numeric strings.""")
            list_of_words.clear()

            for word in list_from_TEXTS_2:
                if word.isnumeric():
                    list_of_words.append(int(word))
            print(f"""The sum of all the numbers {sum(list_of_words)}.""")
            list_of_words.clear()

            print(oddelovac)

            occurences = {}

            for word in list_from_TEXTS_2:
                length_of_word = len(word)
                if length_of_word not in occurences:
                    occurences[length_of_word] = 1
                else:
                    occurences[length_of_word] += 1

            print(
                oddelovac,
                f"   LEN|      OCCURENCES    |NR.   ",
                oddelovac,
                sep="\n"
                )
            
            for index, occurence in sorted(occurences.items()):
                string = str(index)
                print(f"""{" " * 3}{string.rjust(3)}|{occurence * "*"}{" " * (20 - len(occurence * "*"))}|{occurence}""")

        elif number_of_text == 3:

            cutted_words = TEXTS["aaa"].replace(",","").replace(".","")
            list_from_TEXTS_3 = cutted_words.split()

            for word in list_from_TEXTS_3:
                list_of_words.append(word)
            print(f"""There are {len(list_of_words)} words in the selected text.""")
            
            for word in list_from_TEXTS_3:
                list_of_words.append(word.istitle())
                titlecase_words = list_of_words.count(True)
            print(f"""There are {titlecase_words} titlecase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_3:
                if word.isalpha():
                    list_of_words.append(word.isupper())
                    uppercase_words = list_of_words.count(True)
            print(f"""There are {uppercase_words} uppercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_3:
                if word.isalpha():
                    list_of_words.append(word.islower())
                    lowercase_words = list_of_words.count(True)
            print(f"""There are {lowercase_words} lowercase words.""")
            list_of_words.clear()

            for word in list_from_TEXTS_3:
                if word.isnumeric():
                    list_of_words.append(word)
                    numeric_strings = len(list_of_words)
            print(f"""There are {numeric_strings} numeric strings.""")
            list_of_words.clear()

            for word in list_from_TEXTS_3:
                if word.isnumeric():
                    list_of_words.append(int(word))
            print(f"""The sum of all the numbers {sum(list_of_words)}.""")
            list_of_words.clear()

            print(oddelovac)

            occurences = {}

            for word in list_from_TEXTS_3:
                length_of_word = len(word)
                if length_of_word not in occurences:
                    occurences[length_of_word] = 1
                else:
                    occurences[length_of_word] += 1

            print(
                oddelovac,
                f"   LEN|      OCCURENCES    |NR.   ",
                oddelovac,
                sep="\n"
                )
            
            for index, occurence in sorted(occurences.items()):
                string = str(index)
                print(f"""{" " * 3}{string.rjust(3)}|{occurence * "*"}{" " * (20 - len(occurence * "*"))}|{occurence}""")

        else:
            print("error")
    else:
        print("You entered wrong value")
else: 
    print("unregistered user, terminating the programm..")



