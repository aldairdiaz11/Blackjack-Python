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
    """Picks randomly a card from a deck and remove from it"""
    keys = list(deck)
    key = random.choice(keys)
    selected_card = random.choice(deck[key])
    result = (key, selected_card)

    # Delete from deck:
    index = deck[key].index(result[-1])
    deck[key].pop(index)
    return result


class User:
    def __init__(self):
        self.user_points = 0
        self.cards = []

    def add_points(self, card_picked: tuple):
        self.cards.append(card_picked)
        if card_picked[1][0] == 'Ace':
            pass
        else:
            self.user_points += card_picked[1][1]

    def show_cards(self):
        print(f"{self.cards} points: {self.user_points}")

    def __repr__(self):
        return self.cards


# Tests:
# card_random = pick_a_card(cards)
# print(f"removed card: {card_random}")
# print(cards[card_random[0]])
# print(cards[card_random[0]])

if __name__ == '__main__':
    print("Welcome to Blackjack Game")

    play = True
    user = User()
    cpu = User()

    winner = False
    while play:
        # Main game functionality:
        for card in range(2):
            user_new_card = pick_a_card(cards)
            user.add_points(user_new_card)

            cpu_new_card = pick_a_card(cards)
            cpu.add_points(cpu_new_card)

        # Add points:

        print(user.user_points)
        print(cpu.user_points)
        user.show_cards()

        if user.user_points == 21 or cpu.user_points == 21:
            winner = True

        while not winner:
            if cpu.user_points <= 17:
                cpu.add_points(pick_a_card(cards))

            new_card = input('New card? type y, any other key to pass ')
            if new_card == 'y':
                user.add_points(pick_a_card(cards))
                user.show_cards()
            else:
                if user.user_points > cpu.user_points:
                    print("User wins")
                elif user.user_points == cpu.user_points:
                    print("Game tie")
                else:
                    print("Cpu wins")
                winner = True

        # New game:
        user_answer = input("New Game? press 'n' to exit ")
        if user_answer == 'n':
            play = False
        else:
            user.user_points = 0
            cpu.user_points = 0
