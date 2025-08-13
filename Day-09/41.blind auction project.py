logo = r'''
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
print(logo)
once_more = True
while once_more == True:
    dictionary = {}
    name = input("what is your name? ").lower()
    bid = int(input("what is your bid? "))
    dictionary[name] = bid
    should_continue = input("are there any other biders? type 'yes' or 'no'.\n").lower()
    if should_continue == "no":
        once_more = False

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}

# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
def highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    return winner, highest_bid

winner, highest_bid = highest_bidder(dictionary)
print(f"winner is {winner} with a highest bid of {highest_bid}")


