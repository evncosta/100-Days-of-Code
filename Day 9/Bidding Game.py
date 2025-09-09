from art import logo

print(logo)

bidder_info = {}

def defining_bidder():
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidder_info[name] = bid

defining_bidder()

while True:
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if more_bidders == "yes":
        print("\n" * 100)
        print(logo)
        defining_bidder()
    elif more_bidders == "no":
        break
    else:
        print("Invalid input. Type 'yes' or 'no'.")
        continue

winner = max(bidder_info, key=bidder_info.get)
winner_bid = bidder_info[winner]

print("\n" * 100)
print(logo)
print(f"The winning bid is ${winner_bid} from {winner}!")
