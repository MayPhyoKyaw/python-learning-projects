import random
from art import logo
from welcome_art import welcome_text
import os

os.environ['TERM'] = 'xterm-256color'

def deal_card():
    """ Return a random card from the deck. """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def display_cards(user_cards, user_score, dealer_cards):
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

def compare(user_score, computer_score):
    if user_score == computer_score:
        print("Draw 🙃")
    elif computer_score == 0:
        print("Lose, opponent has Blackjack 😱")
    elif user_score == 0:
        print("Win with Blackjack 😎")
    elif user_score > 21:
        print("You went over. You lose 😭")
    elif computer_score > 21:
        print("Opponent went over. You win 😁")
    elif user_score > computer_score:
        print("You win 😃")
    else:
        print("You lose 😤")

def display_final_cards(user_cards, computer_cards, user_score, computer_score):
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
        
    user_score = calculate_scores(user_cards)
    computer_score = calculate_scores(computer_cards)
    display_cards(user_cards, user_score, computer_cards)

    while not is_game_over:
        user_score = calculate_scores(user_cards)
        computer_score = calculate_scores(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            display_cards(user_cards, user_score, computer_cards)
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True
        
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_scores(computer_cards)

    display_final_cards(user_cards, computer_cards, user_score, computer_score)
    compare(user_score, computer_score)

print(welcome_text)
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('clear')
    play_game()