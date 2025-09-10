# Silent Auction - Collects bids and determines the highest bidder
from art import logo

print(logo)

bidder_info = {}

# Function to collect bidder name and bid amount
def defining_bidder():
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bidder_info[name] = bid

# Collect first bidder information
defining_bidder()

# Continue collecting bids until no more bidders
while True:
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()

    if more_bidders == "yes":
        print("\n" * 100)  # Clear screen for privacy
        print(logo)
        defining_bidder()
    elif more_bidders == "no":
        break
    else:
        print("Invalid input. Type 'yes' or 'no'.")
        continue

# Determine winner with the highest bid
winner = max(bidder_info, key=bidder_info.get)
winner_bid = bidder_info[winner]

# Display final result
print("\n" * 100)
print(logo)
print(f"The winning bid is ${winner_bid} from {winner}!")
