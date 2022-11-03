import art
import random
import os

deck = {
    'A': 11,
    'J': 10,
    'K': 10,
    'Q': 10,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10
    }

deck_list = ['A', 'J', 'K', 'Q', '2', '3', '4', '5', '6', '7', '8', '9', '10']

player_hand = []
handler_hand = []

def first_player_hand():
    for card in range(2):
        player_hand.append(random.choice(deck_list))

def f_handler_hand():
    for card in range(1):
        handler_hand.append(random.choice(deck_list))

def hit():
    player_hand.append(random.choice(deck_list))

def player_sum():
    p_sum = 0
    for card in player_hand:
        p_sum += deck[card]
    if p_sum > 21 and player_hand.count('A') > 0:
        p_sum -= 10
    return p_sum

def handler_sum():
    h_sum = 0
    for card in handler_hand:
        h_sum += deck[card]
    if h_sum > 21 and handler_hand.count('A') > 0:
        h_sum -= 10
    return h_sum

def result():
    os.system('cls||clear')
    print(art.logo)
    print(f"Your cards: {player_hand} current score: {player_sum()}")
    print(f"Computer's card is {handler_hand} current score: {handler_sum()}")

print(art.logo)
first_player_hand()
f_handler_hand()
i_hit = 'y'
result()

while player_sum() < 21 and handler_sum() < 17:
    if i_hit == 'y':
        i_hit = input("Type 'y' to get another card, type 'n' to pass: ")
    if i_hit == 'y':
        hit()
    if player_sum() < 21 and i_hit == 'y':
        result()
    if i_hit == 'n':
        while handler_sum() < 17:
            f_handler_hand()
        break

if player_sum() <= 21:
  while handler_sum() < 17:
    f_handler_hand()

if player_sum() > 21 or handler_sum() > player_sum() and handler_sum() <= 21:            
  result()
  print("You lose")
elif player_sum() == handler_sum():
  result()
  print("Draw") 
else:
  result()
  print("You win") 
