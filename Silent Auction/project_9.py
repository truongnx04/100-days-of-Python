import art

print(art.LOGO)

def find_highest_bidder(bidder_dictionary):
    bid_highest = 0
    winner = ""

    for bidder in bidder_dictionary:
        bid_amount = bidder_dictionary[bidder]
        if bid_amount > bid_highest:
            bid_highest = bid_amount
            winner = bidder

    print(f"The winner is {winner} with a bid of ${bid_highest}.")


info_bidder = {}
user_continue = True

while user_continue:
    name = input("What is your name?: ")
    bid = int(input("What is your bid? $"))
    info_bidder[name] = bid

    should_continue = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    if should_continue == "no":
        user_continue = False
        find_highest_bidder(info_bidder)
    elif should_continue == "yes":
        print("\n" * 20)
    