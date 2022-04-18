# Created by Diego Perez
# Date: 2-28-2022
# HW 4


# FUNCTIONS
def reverse_string(word):
    # tmp_string_buffer = ""
    # for i in range(len(word) - 1, -1, -1):
    #     tmp_string_buffer += word[i]

    # return tmp_string_buffer

    return word[::-1]

def is_palindrome(word):
    if (word == reverse_string(word)):
        return True
    else: 
        return False

def is_prime(num):

    # Account for numbers lower than or equal to 1
    if (num <= 1):
        return False

    count = num - 1

    while (count >= 2):
        if (num % count == 0):
            return False
        
        count -= 1
    
    # If the function didn't terminate or break out of the loop, then the number is prime
    return True

def is_emirp(num):
    # Must use previous 3 functions

    num_as_string = str(num)
    num_as_string_reversed = reverse_string(num_as_string)

    if (not is_prime(num)):
        # Return false if num is not a prime number
        return False
    else:
        # num is a prime number

        # The number 11 is not an emirp because it is the same in reverse
        if (num_as_string == num_as_string_reversed):
            return False
        # elif (is_palindrome(num_as_string)): # Unnecessary
        else:

            # We already checked if num is a prime number
            if (is_prime(int(num_as_string_reversed))):
                return True
            else:
                return False


# ORGANIZATIONAL MAIN FUNCTION HELPERS
def reverse_word():
    # Ask the user for a word, then prints that word in reverse
    for i in range(2):
        user_input = input("Enter a word that you want to reverse: ")
        print(reverse_string(user_input) + "\n")

def check_palindrome():
    # Asks the user for a word, then tells the user if it is a palindrome... "Palindrome!" or "Not a palindrome!"
    for i in range(3):
        user_input = input("Check for palindrome: ")
        if (is_palindrome(user_input)):
            print("Palindrome!\n")
        else:
            print("Not a palindrome!\n")

def check_prime():
    # Ask the user for a number, then tell them if it is prime... "Prime!" or "Not a prime!"
    for i in range(2):
        user_input = int(input("Check for prime number: "))
        if (is_prime(user_input)):
            print("Prime!\n")
        else:
            print("Not a prime!\n")

def check_emirp():
    # Ask the user for a number, then tell them if it is emirp... "Emirp!" or "Not an emirp!"
    for i in range(3):
        user_input = int(input("Check for emirp number: "))
        if (is_emirp(user_input)):
            print("Emirp!\n")
        else:
            print("Not an emirp!\n")


# BONUS FUNCTIONS
def are_twin_primes(num_1, num_2):
    # A pair of primes that are 2 numbers away such as 5 and 7
    if (abs(num_1 - num_2) <= 2):
        if (is_prime(num_1) and is_prime(num_2)):
            return True
        else: 
            return False
    else: 
        return False

def part_of_twin_prime_pair(num):
    lower_range = num - 2
    upper_range = num + 2

    lower_range_twin_prime_pair = False
    upper_range_twin_prime_pair = False

    if (are_twin_primes(lower_range, num)):
        # return True
        lower_range_twin_prime_pair = True
        # print("Twin Prime: {}, {}\n".format(lower_range, num))

    if (are_twin_primes(num, upper_range)):
        # return True
        upper_range_twin_prime_pair = True
        # print("Twin Prime: {}, {}\n".format(num, upper_range))

    # Format the output nicely
    if (lower_range_twin_prime_pair):
        if (upper_range_twin_prime_pair):
            print("Twin Prime: {}, {}".format(lower_range, num))
            print("Twin Prime: {}, {}\n".format(num, upper_range))
        else:
            print("Twin Prime: {}, {}\n".format(lower_range, num))
    elif (upper_range_twin_prime_pair):
        print("Twin Prime: {}, {}\n".format(num, upper_range))

    if ((not lower_range_twin_prime_pair) and (not upper_range_twin_prime_pair)):
    # if (not (lower_range_twin_prime_pair or upper_range_twin_prime_pair)):
        # return False
        print("{} is not part of a twin prime pair.\n".format(num))


# UTILITIES
def main_function_section_separator(character, length):
    for i in range(length):
        print(character, end="")
    print("\n")


def main():

    reverse_word()

    main_function_section_separator("=", 20)

    check_palindrome()

    main_function_section_separator("=", 20)

    check_prime()

    main_function_section_separator("=", 20)

    check_emirp()

    main_function_section_separator("=", 20)

    for i in range(2):
        user_input = int(input("Check for twin prime pair: "))
        part_of_twin_prime_pair(user_input)


if __name__ == "__main__":
    main()