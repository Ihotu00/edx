# dictionary of all the fruits and their calories
fruits = {
    "apple": "130", "avocado": "50", "banana": "110", "cantaloupe": "50",
    "grapefruit": "60", "grapes": "90", "honeydew": "50", "melon": "50",
    "kiwifruit": "90", "lemon": "15", "lime": "20", "nectarine": "60",
    "orange": "80", "peach": "60", "pear": "100", "pineapple": "50",
    "plums": "70", "strawberries": "50", "sweet cherries": "100",
    "tangerine": "50", "watermelon": "80",
}

 # accept user input
item = input("Item: ").lower()

# find input in the dict and print out the corresponding calories
if item in fruits:
    print("Calories: ", fruits[item])