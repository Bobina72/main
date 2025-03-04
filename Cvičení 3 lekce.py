slovník = {
    "ball":"míč",
    "cat":"kočka",
    "dog":"pes",
    "key":"klíče",
    "house":"dům",
    "apple": "jablko",
    "banana": "banán",
    "carrot": "mrkev",
    "dog": "pes",
    "cat": "kočka",
    "house": "dům",
    "car": "auto",
    "train": "vlak",
    "bicycle": "kolo",
    "computer": "počítač",
    "phone": "telefon",
    "table": "stůl",
    "chair": "židle",
    "window": "okno",
    "door": "dveře",
    "book": "kniha",
    "pen": "pero",
    "paper": "papír",
    "sun": "slunce",
    "moon": "měsíc",
    "water": "voda",
    "fire": "oheň",
    "earth": "země",
    "air": "vzduch",
    "food": "jídlo",
    "drink": "nápoj",
    "music": "hudba",
    "friend": "přítel",
    "family": "rodina",
    "school": "škola",
    "work": "práce",
    "money": "peníze",
    "happiness": "štěstí",
    "love": "láska",
    "time": "čas",
    "day": "den",
    "night": "noc",
    "week": "týden",
    "month": "měsíc",
    "year": "rok"
    }
#print("Anglická slova:", slovník.keys())
#print("České překlady", slovník.values())

slovo = input("Zadej anglické slovo k překladu:").lower()
if slovo in slovník:
    print(f"Překlad: {slovník[slovo]}")
else:
    print("Slovo se ve slovníku nenachází")