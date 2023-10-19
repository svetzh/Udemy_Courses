from game_data import data
from art import logo, vs
import random

previous_account = None
def get_random_account():
    global previous_account
    while True:
        account = random.choice(data)
        if account != previous_account:
            previous_account = account
            return account

def check_answer(guess, a_count, b_count):
    if a_count > b_count:
        return guess == "a"
    elif a_count < b_count:
        return guess == "b"

def game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:

        account_a = account_b
        account_b = get_random_account()

        print(f"Compare A: {account_a['name']}, a {account_a['description']}, from {account_a['country']}")
        print(vs)
        print(f"Against B: {account_b['name']}, a {account_b['description']}, from {account_b['country']}")

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a['follower_count']
        b_follower_count = account_b['follower_count']
        correct = check_answer(user_input, a_follower_count, b_follower_count)

        if correct:
            score += 1
            print(f"You are right! Current score: {score}")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue = False


game()