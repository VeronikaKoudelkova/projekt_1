"""
projekt_1.py: první projekt do Engeto Online Python Akademie
author: Veronika Koudelkova
email: koudelkova.veronika87@gmail.com
discord: Veronika K.#4490
"""
TEXTS = {
    "1": """Situated about 10 miles west of Kemmerer,
        Fossil Butte is a ruggedly impressive
        topographic feature that rises sharply
        some 1000 feet above Twin Creek Valley
        to an elevation of more than 7500 feet
        above sea level. The butte is located just
        north of US 30N and the Union Pacific Railroad,
        which traverse the valley.""",
    "2": """At the base of Fossil Butte are the bright
        red, purple, yellow and gray beds of the Wasatch
        Formation. Eroded portions of these horizontal
        beds slope gradually upward from the valley floor
        and steepen abruptly. Overlying them and extending
        to the top of the butte are the much steeper
        buff-to-white beds of the Green River Formation,
        which are about 300 feet thick.""",
    "3": """The monument contains 8198 acres and protects
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


if jmeno in registered_users and heslo == registered_users[jmeno]:                
    print(f"""Welcome to the app, {jmeno}.\nWe have 3 texts to be analyzed.""")
    print("Enter a number btw. 1 and 3 to select:")

    number_of_text = input()

    if number_of_text in TEXTS.keys():                       

        oddelovac = "-" * 50
        print(oddelovac)

        cutted_words = TEXTS[number_of_text].replace(",","").replace(".","")            
        list_from_TEXTS = cutted_words.split()
        list_of_words = list()
        list_of_numbers = list()
        
        for word in list_from_TEXTS:


            if word.istitle():
                list_of_words.append("Titlecase")
                continue

            elif word.isupper():
                list_of_words.append("UPPERCASE")
                continue

            elif word.islower():
                list_of_words.append("lowercase")
                continue

            elif word.isnumeric():
                list_of_words.append("numeric_string")
                list_of_numbers.append(int(word))

                continue
                
        print(f"""There are {len(list_from_TEXTS)} words in the selected text.""")
        print(f"""There are {list_of_words.count("Titlecase")} titlecase words.""")
        print(f"""There are {list_of_words.count("UPPERCASE")} uppercase words.""")
        print(f"""There are {list_of_words.count("lowercase")} lowercase words.""")
        print(f"""There are {list_of_words.count("numeric_string")} numeric string.""")
        print(f"""The sum of all the numbers {sum(list_of_numbers)}.""")
    

        print(oddelovac)

        occurences = {}

        for word in list_from_TEXTS:
            length_of_word = len(word)
            if length_of_word not in occurences:
                occurences[length_of_word] = 1
            else:
                occurences[length_of_word] += 1

        print(
            oddelovac,
            f"   LEN|     OCCURENCES     |NR.   ",
            oddelovac,
            sep="\n"
            )
            
        for index, occurence in sorted(occurences.items()):
            string = str(index)
            print(f"""{" " * 3}{string.rjust(3)}|{occurence * "*"}{" " * (20 - len(occurence * "*"))}|{occurence}""")

    else:
        print("You entered wrong value!")
    
else: 
    print("unregistered user, terminating the programm..")





      