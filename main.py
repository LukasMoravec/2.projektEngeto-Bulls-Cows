import random

import time

TXT_SEPARS = 50 * "-"
GUESS_LENGTH = 4

def generate_number() -> str:
    """
    Generates a secret 4 digit number, first digit will never be 0, numbers will never repeat
    """
    numbers = list(range(10))
    first_number = random.sample(range(1, 10), 1)
    numbers.remove(first_number[0])
    second_to_fourth_numbers = random.sample(numbers, 3)
    generated_number = "".join(map(str, first_number)) + "".join(map(str, second_to_fourth_numbers))
    return generated_number

def validate_guess(guess: str) -> bool:
    """
    Validates the player's guess.
    Checks that it contains exactly four digits, doesn't start with 0,
    and doesn't contain duplicate digits.
    """
    if len(guess) != GUESS_LENGTH:
        print(f"Your guess must be 4 digits! Please try again.\n{TXT_SEPARS}")
        return False
    elif not guess.isdigit():
        print(f"Your guess must be only numbers! Please try again.\n{TXT_SEPARS}")
        return False
    elif guess[0] == "0":
        print(f"Your guess mustn't start with 0! Please try again.\n{TXT_SEPARS}")
        return False
    elif len(set(guess)) != GUESS_LENGTH:
        print(f"Your guess mustn't have duplicates! Please try again.\n{TXT_SEPARS}")
        return False
    else:
        return True

def validate_answer_for_play_again(play_again: str) -> bool:
    """
    Validates the answer of the player to question if they would like to play again. 
    """
    if play_again != "y" and play_again != "n":
        print(f"Your answer must be only 'y' or 'n'! Please try again.\n{TXT_SEPARS}")
        return False
    else:
        return True

def calculate_bulls_and_cows(guess: str, generated_number: str) -> tuple:
    """
    Calculates, how many bulls and cows have the player guessed in the last guess.
    """
    bulls = 0
    cows = 0
    for i in range(GUESS_LENGTH):
        if guess[i] == generated_number[i]:
            bulls += 1
        if guess[i] in generated_number and guess[i] != generated_number[i]:
            cows += 1
    return bulls, cows

def main() -> None:
    stats_guesses = []
    stats_timers = []
    play_again = "y"
    while play_again == "y":
        generated_number = generate_number()
        bulls = 0
        tries = 0
        start_time = time.perf_counter()
        print(
        f"Hi there!\n"
        f"{TXT_SEPARS}\n"
        f"I've generated a random 4 digit number for you.\n"
        f"Let's play a bulls and cows game.\n"
        f"{TXT_SEPARS}"
        )
        while bulls != GUESS_LENGTH:
            guess = input("Enter a number: ")
            tries += 1
            while not validate_guess(guess):
                guess = input("Enter a number: ")
            bulls, cows = calculate_bulls_and_cows(guess, generated_number)
            print_bulls = "bull" if bulls == 1 else "bulls"
            print_cows = "cow" if cows == 1 else "cows"
            print(f"{print_bulls}: {bulls}, {print_cows}: {cows}\n{TXT_SEPARS}")  
        else:
            end_time = time.perf_counter()
            duration_of_game = end_time - start_time
            stats_guesses.append(tries)
            stats_timers.append(duration_of_game)
            print(
            f"Correct, you've guessed the right number\n"
            f"in {tries} guesses!\n"
            f"It took you {duration_of_game:.1f} seconds!\n"
            f"{TXT_SEPARS}\n"
            f"That's amazing!"
            )
            if len(stats_guesses) > 1:
                print("Statistics of previous games:")
                for i, stat in enumerate(stats_guesses, 1):
                    print(f"{i}. game = {stat} guesses, time: {stats_timers[i - 1]:.1f} s.")
            print(TXT_SEPARS)
            play_again = input(f"Do you wish to play again? (y / n): ")
            while not validate_answer_for_play_again(play_again):
                play_again = input(f"Do you wish to play again? (y / n): ")
    else:
        print(f"{TXT_SEPARS}\nThank you for playing!\n")

if __name__ == "__main__":
    main()