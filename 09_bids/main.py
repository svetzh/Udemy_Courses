from art import logo
import os

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
# Call the clear_console() function whenever you want to clear the console.

def find_highest_bidder(bidding_record):
    for bidder in bidding_record.values():
        bid_amount = bidding_record[bidder]


print(logo)

bids = {}
bidding_finished = False

while not bidding_finished:
    name = input("What is your name? ")
    price = int(input("What is your bit? $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.")
    if should_continue == "no":
        bidding_finished = True
    elif should_continue == "yes":
        clear_console()



