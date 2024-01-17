import os

def clear_console():
    # Print new lines for visual separation, as clearing might not work in some IDEs
    print("\n" * 5)

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

def bidding_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

print(logo)
print("Welcome to secret auction program!")

active_bidding = {}
bidding_continue = False

while not bidding_continue:
    name = input("What is your name?\n").lower()
    bid = int(input("What is your bid? $\n"))  # Consider adding input validation here
    active_bidding[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()

    if should_continue == "no":
        bidding_continue = True
    clear_console()
    print(logo)

bidding_winner(active_bidding)
