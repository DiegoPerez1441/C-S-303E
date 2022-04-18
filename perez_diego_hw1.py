from blessings import Terminal
term = Terminal()


# UTILITIES
def case_insensitive_in(key, list):
    return key.upper() in map(str.upper, list)

choose_prompt = lambda choice_selection : "Choose: " + str(choice_selection) + ": "

def input_prompt(prompt, choices):
    # print(choices)
    # return input(prompt + "\n" + choose_prompt(choices))

    # while choice doesn't match choices, keep asking user for a valid choice with a while loop
    # Validate user input by converting input to lowercase
    choice = None
    # while (choice is None or not(case_insensitive_in(choice, choices))):
    while (True):
        choice = input(prompt + "\n" + choose_prompt(choices))
        print()

        if (not(case_insensitive_in(choice, choices))):
            print(term.red("Invalid Answer. Please try again."))
        else:
            # Get the index of the choice and output the choice from the original choices list
            tmp_choices_upper = [x.upper() for x in choices]
            index = tmp_choices_upper.index(choice.upper())

            # return choice
            return choices[index]


# QUESTIONS
def questions():
    platform_choices = ["Web", "Games", "AI", "General"]
    platform_choice = input_prompt("What kind of platform do you want to develop for?", platform_choices)

    if (platform_choice == "Web"):
        web_choices = ["Web Only", "Cross Platform"]
        web_choice = input_prompt("What kind of web development do you want to do?", web_choices)

        if (web_choice == "Web Only"):
            print("Learn HTML5, JavaScript, and CSS3.")
        elif (web_choice == "Cross Platform"):
            print("Learn React Native, HTML5, JavaScript, CSS3, and NodeJS.")

    elif (platform_choice == "Games"):
        games_choices = ["Mobile", "Desktop"]
        games_choice = input_prompt("What kind of platforms do you want to develp games for?", games_choices)

        if (games_choice == "Mobile"):
            print("Learn Swift for iOS and Java for Android.")
        elif (games_choice == "Desktop"):
            print("Learn C++.")

    elif (platform_choice == "AI"):
        print("Learn Python3.")
    elif (platform_choice == "General"):
        print("You can learn a lot of programming languages for general purpose, but Python3 and Java are recommended by the community.")
    else:
        print(term.red("[Exception Raised]: Please restart program."))


# PROGRAM START
program_initialized = False
is_awesome_program = True

print("This is a 30 second quiz to suggest what programming languages to learn for certain cases.")
program_initialized_choice = input_prompt("Ready to start?", ["y", "n"])

if (program_initialized_choice == "y"):
    program_initialized = True
else:
    program_initialized = False

if (program_initialized and is_awesome_program):
    questions()