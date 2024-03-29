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
    def __init__(self, name: str):
        self.user_points = 0
        self.cards = []
        self.user_name = name

    def add_points(self, card_picked: tuple):
        self.cards.append(card_picked)
        if card_picked[1][0] == 'Ace':
            if self.user_points > 21:
                self.user_points += 1
            else:
                self.user_points += 11
        else:
            self.user_points += card_picked[1][1]

        if ("Ace", 11, 1) in self.cards and self.user_points > 21:
            self.user_points -= 11 * self.cards.count(("Ace", 11, 1))

    def restart(self):
        self.user_points = 0
        self.cards = []

    def show_cards(self):
        print(f"{self.user_name}: {self.cards} points: {self.user_points}")

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
    user = User('Player 1')
    cpu = User('CPU')

    winner = ''
    while play:
        # Main game functionality:
        for card in range(2):
            user_new_card = pick_a_card(cards)
            user.add_points(user_new_card)

            cpu_new_card = pick_a_card(cards)
            cpu.add_points(cpu_new_card)

        # Show first cards:
        print(cpu.cards[0])
        user.show_cards()

        if user.user_points == 21 or cpu.user_points == 21:
            if user.user_points > cpu.user_points:
                winner = user.user_name
            else:
                winner = cpu.user_name

        while not winner:
            if cpu.user_points <= 17:
                cpu.add_points(pick_a_card(cards))
                if cpu.user_points > 21:
                    winner = cpu.user_name
                    continue

            new_card = input('New card? type y, any other key to pass ')
            if new_card == 'y':
                user.add_points(pick_a_card(cards))
                user.show_cards()

                if user.user_points == 21:
                    winner = user.user_name
                elif user.user_points > 21:
                    winner = cpu.user_name
            else:
                if user.user_points > cpu.user_points:
                    winner = user.user_name
                elif user.user_points == cpu.user_points:
                    winner = 'tie'
                else:
                    winner = cpu.user_name

        # User winner
        print(f"\nWinner: {winner}")
        user.show_cards()
        cpu.show_cards()

        # New game:
        user_answer = input("New Game? press 'n' to exit ")
        if user_answer == 'n':
            play = False
        else:
            print("\n\n")
            winner = ''
            user.restart()
            cpu.restart()
