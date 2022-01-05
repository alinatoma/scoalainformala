import random

with open('cards.txt', 'r') as f:
    cards = [line.strip() for line in f]

print(cards)

if len(cards) < 10:
  raise Exception("Sorry, not enough cards to play the game")
else:
    print("You can play the game!")

shuffled_cards = random.sample(cards, k=len(cards))

print(shuffled_cards)

print(f"Randomly selected card is: {random.choice(shuffled_cards)}")