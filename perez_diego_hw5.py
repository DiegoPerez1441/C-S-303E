# Author: Diego Perez
# Date: 3-5-2022
# HW 5

recipes = {
    "Chicken Soup": ["chicken", "chicken broth", "carrots", "celery", "noodles"],
    "Spaghetti": ["spaghetti noodles", "pasta sauce", "meatballs"],
    "Grilled Cheese": ["bread", "butter", "cheese"],
    "Garden Salad": ["lettuce", "cucumber", "carrots", "olives"],
    "Diego's Special": ["coffee", "sugar", "half and half"]
}

grocery_list = []

def print_grocery_list():
    ingredients = ", ".join(grocery_list)
    output = "Grocery List: " + ingredients

    print(output)

def add_to_grocery_list():
    while (True):
        user_input = input("Would you like to add any other items to your grocery list? [Enter 'Done' when finished]: ")
        if (user_input == "Done"):
            # Print a new line to separate output
            print()
            print_grocery_list()
            break
        else:
            grocery_list.append(user_input)
            continue

def print_recipe(recipe):
    ingredients = ", ".join(recipes[recipe])
    output = str(recipe) + ": " + ingredients

    grocery_list.extend(recipes[recipe])

    print(output)

def choose_recipe(counter, total):
    while (True):
        recipe_list = ", ".join(recipes.keys())
        prompt = f"[{counter}/{total}] " \
                "What would you like to make? " \
                f"(Choose: {recipe_list})\n" \
                "[Choice]: "

        user_input = input(prompt)

        if (user_input in recipes.keys()):
            print_recipe(user_input)
            break
        else:
            print("Invalid Recipe Name. Please Try Again.\n")
            continue

def main():
    for i in range(2):
        choose_recipe(i + 1, 2)

        # Print a new line to separate output
        print()

        print_grocery_list()

    # Print a new line to separate output
    print()

    add_to_grocery_list()


if __name__ == "__main__":
    main()