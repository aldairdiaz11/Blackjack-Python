# CS 101 Portfolio project: Python Terminal Game
import random

card_values = [("Ace", 11, 1), ("King", 10), ("Queen", 10), ("Jack", 10), ("10", 10),
               ("9", 9), ("8", 8), ("7", 7), ("6", 6), ("5", 5), ("4", 4), ("3", 3), ("2", 2)]

cards = {
    "Hearts": card_values,
    "Diamonds": card_values,
    "Clover": card_values,
    "Pikes": card_values
}


def pick_a_card(deck: dict):
    keys = list(deck)
    key = random.choice(keys)
    card = random.choice(deck[key])
    result = (key, card)
    return result


def remove_card_from_deck(result: tuple, deck: dict):
    values = deck[result[0]]
    card_index = values.index(result[-1])
    deck[result[0]].pop(card_index)


def game_functionality():
    pass


# Tests:
card_random = pick_a_card(cards)
print(f"removed card: {card_random}")
print(cards[card_random[0]])
remove_card_from_deck(card_random, cards)
print(cards[card_random[0]])


if __name__ == '__main__':
    print("Welcome to Blackjack Game")

    play = True
    while play:
        # Main game functionality:

        # New game:
        user_answer = input("New Game? press 'n' to exit ")
        if user_answer == 'n':
            play = False
