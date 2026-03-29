## Project - Highest Bidder

# Solution - 

import art
print(art.logo)
bids = {}
yes_no = True

def compare_bids(biding_dict):
    high_bid = 0
    winner = ""
    for bidder in biding_dict:
        bid_amount = biding_dict[bidder]
        if bid_amount > high_bid:
            high_bid = bid_amount
            winner = bidder



    print(f"The winner is {winner} with a bid of ${high_bid}.")

while yes_no:
    user_name = input("What is your name? ")
    bid = int(input("What's your bid?: $"))
    bids[user_name] = bid
    yes_no = input("Are there any other bidders? Type 'yes' or 'no'. \n").lower()
    if yes_no == "no":
        print("\n" * 20)
        yes_no = False
        compare_bids(bids)
    elif yes_no == "yes":
        print("\n" * 20)



