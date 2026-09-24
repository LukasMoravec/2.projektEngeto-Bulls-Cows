import random

def generate_number() -> int:
    """
    Generates a secret 4 digit number, first digit will never be 0, numbers will never repeat
    """
    numbers = list(range(10))
    first_number = random.sample(range (1, 10), 1)
    numbers.remove(first_number[0])
    second_to_fourth_numbers = random.sample(numbers, 3)
    generated_number = "".join(map(str, first_number)) + "".join(map(str, second_to_fourth_numbers))
    return int(generated_number)

def validate_guess(guess) -> bool:
    """
    Validates the player's guess.
    Checks that it contains exactly four digits, doesn't start with 0,
    and doesn't contain duplicate digits.
    """
    if len(guess) != 4:
        print("Your guess must be 4 digits! Please try again.")
        print(txt_separs)
        return False
    elif not guess.isdigit():
        print("Your guess must be only numbers! Please try again.")
        print(txt_separs)
        return False
    elif guess[0] == "0":
        print("Your guess mustn't start with 0! Please try again.")
        print(txt_separs)
        return False
    elif len(set(guess)) != 4:
        print("Your guess mustn't have duplicates! Please try again.")
        print(txt_separs)
        return False
    else:
        return True

txt_separs = "-----------------------------------------------"
generated_number = str(generate_number())
bulls = 0 # if the player guesses correctly the numbers and its position
cows = 0 # if the player guesses correctly the number but not the position
tries = 0

print("Hi there!")
print(txt_separs)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print(txt_separs)

while bulls != 4:
    guess = input("Enter a number: ")
    bulls = 0
    cows = 0
    tries += 1
    while not validate_guess(guess):
        guess = input("Enter a number: ")

    for i in range(4):
        if guess[i] == generated_number[i]:
            bulls += 1

    for i in range(4):
        if guess[i] in generated_number and guess[i] != generated_number[i]:
            cows += 1
    print(f"bulls: {bulls}, cows: {cows}")
    print(txt_separs)
else:
    print("Correct, you've guessed the right number")
    print(f"in {tries} guesses!")
    print(txt_separs)
    print("That's amazing!")