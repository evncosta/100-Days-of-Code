import random
from art import logo

def play_blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    user_cards = random.sample(cards, 2)
    computer_cards = random.sample(cards, 2)

    user_score = sum(user_cards)
    computer_score = sum(computer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")

    if user_score == 21:
        print("You have a blackjack! You win!")
        return
    elif computer_score == 21:
        print("The computer has a blackjack! You lose...")
        return

    while True:
        answer = input("Do you want to draw another card (y/n)? ").lower()

        if answer == "y":
            new_card = random.choice(cards)
            user_cards.append(new_card)
            user_score = sum(user_cards)

            print(f"You drew a {new_card}. Your cards: {user_cards}, current score: {user_score}")

            if user_score > 21:
                while 11 in user_cards and user_score > 21:
                    ace_index = user_cards.index(11)
                    user_cards[ace_index] = 1
                    user_score = sum(user_cards)
                    print(f"Your Ace now counts as 1. Your cards: {user_cards}, current score: {user_score}")

                if user_score > 21:
                    print("You went over 21! You lose...")
                    return
        else:
            break

    while computer_score < 17:
        new_card = random.choice(cards)
        computer_cards.append(new_card)
        computer_score = sum(computer_cards)
        print(f"Computer drew a {new_card}. Computer's cards: {computer_cards}, current score: {computer_score}")

        while computer_score > 21 and 11 in computer_cards:
            ace_index = computer_cards.index(11)
            computer_cards[ace_index] = 1
            computer_score = sum(computer_cards)
            print(f"Computer's Ace now counts as 1. Computer's cards: {computer_cards}, current score: {computer_score}")

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

    if computer_score > 21:
        print("Computer went over 21! You win!")
    elif user_score > computer_score:
        print("You got a higher score! You win!")
    elif user_score < computer_score:
        print("The computer got a higher score! You lose...")
    else:
        print("It's a draw!")

while True:
    print(logo)
    start = input("Do you want to play Blackjack (y/n)? ").lower()

    if start == "y":
        play_blackjack()
    elif start == "n":
        break
    else:
        print("Invalid output. Write 'y' for yes and 'n' for no.")