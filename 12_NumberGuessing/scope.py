from random import randint

EASY_MODE = 10
HARD_MODE = 5

def check_answer(guess_number, ans_num, remaining_nums):
    if guess_number > ans_num:
        print("Too high!")
        return remaining_nums - 1
    elif guess_number < ans_num:
        print("Too low!")
        return remaining_nums - 1
    else:
        print(f"You got it the answer is : {ans_num}")


def set_difficulty():
    level = input("Choose difficulty. 'easy' or 'hard'! ").lower()
    if level == "easy":
        return EASY_MODE
    elif level == "hard":
        return HARD_MODE


def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    answer_num = randint(1, 100)
    print(f"The correct answer is: {answer_num}")

    turns = set_difficulty()
    guess_num = 0
    while guess_num != answer_num:

        guess_num = int(input("Make a guess: "))

        turns = check_answer(guess_num, answer_num, turns)
        if turns == 0:
            print("You run out of guesses. You lose.")
            return
        elif guess_num != answer_num:
            print("Guess again!")

game()

