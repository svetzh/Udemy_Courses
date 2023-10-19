from art import logo
import random
import os

BLACKJACK = 21

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    if sum(cards) == BLACKJACK and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(u_score, com_score):
    if u_score == com_score:
        return "Draw 🙃"
    elif com_score == 0:
        return "You lose. Opponent has Black-jack 😱"
    elif u_score == 0:
        return "Win with a 11_Blackjack 😎"
    elif u_score > 21:
        "You went over. You lose 😭"
    elif com_score > 21:
        return "Opponent went over. You win 😁"
    elif u_score > com_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer first card: {computer_cards[0]}")

        if user_score == 0 or comp_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input(f"Do you want to play a game of 11_Blackjack? Type 'y' or 'n'? "):
    clear_console()
    play_game()
