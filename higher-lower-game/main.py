from game import data
from art import logo, vs
import random
import os

os.environ['TERM'] = 'xterm-256color'

score = 0
game_should_continue = True

print(logo)

def format_data(data):
    """Format the data into printable format."""
    name = data['name']
    description = data['description']
    country = data['country']
    return f"{name}, {description}, from {country}"

def check_answer(guess_input, a_follower_count, b_follower_count):
    if a_follower_count > b_follower_count:
        return guess_input == "a"
    else:
        return guess_input == "b"
    
def display(a_data, b_data):
    print(f"Compare A: {format_data(data=a_data)}")
    print(vs)
    print(f"Against B: {format_data(data=b_data)}")
    
while game_should_continue:
    a_data = random.choice(data)
    b_data = random.choice(data)
    if a_data == b_data:
        b_data = random.choice(data)
        
    display(a_data, b_data)
        
    a_follower_count = a_data['follower_count']
    b_follower_count = b_data['follower_count']
    guess_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    is_correct = check_answer(guess_input, a_follower_count, b_follower_count)
    os.system('clear')
    print(logo)
    
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"Sorry, that's wrong. Final score: {score}.")