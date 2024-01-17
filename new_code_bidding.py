import os


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    bid = int(input("What is your bid? $\n"))
    active_bidding[name] = bid
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        bidding_continue = True
    elif should_continue == "yes":
        active_bidding.clear()

    clear_console()
    print(logo)

bidding_winner(active_bidding)
