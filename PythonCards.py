import random

class CardStack:
    def __init__(self):
        self.cards_on_stack = {"Spades": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                               "Hearts": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                               "Clubs": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"],
                               "Diamonds": ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King",
                                            "Ace"]}
        self.cards_in_play = {"Spades": [], "Hearts": [], "Clubs": [], "Diamonds": []}

    def __str__(self):
        return str(self.cards_on_stack)

    def __repr__(self):
        return str(self.cards_on_stack)

    def get_cards_in_play(self):
        return self.cards_in_play

    def get_cards_on_stack(self):
        return self.cards_on_stack

    def get_number_of_cards_on_stack(self):
        count = 0
        for suit in self.cards_on_stack:
            count += len(self.cards_on_stack[suit])
        return count

    def get_number_of_cards_in_play(self):
        count = 0
        for suit in self.cards_in_play:
            count += len(self.cards_in_play[suit])
        return count
    def draw(self, amount):
        output = []
        if amount > 52 or amount < 0:
            raise ValueError("Error: Amount is not between 0 and 52")
        if amount > self.get_number_of_cards_on_stack():
            raise ValueError("Error: Not enough cards on stack")
        for i in range(amount):
            suit = random.choice(list(self.cards_on_stack.keys()))
            while True:
                if len(self.cards_on_stack[suit]) == 0:
                    suit = random.choice(list(self.cards_on_stack.keys()))
                else:
                    break
            card = random.choice(self.cards_on_stack[suit])
            self.cards_in_play[suit].append(card)
            self.cards_on_stack[suit].remove(card)
            output.append(tuple([suit, card]))
        return output



def get_cards_in_play(Stack):
    if type(Stack) != CardStack:
        raise TypeError("Error: Object is not a Card Stack")
    else:
        return Stack.get_cards_in_play()

def get_cards_on_stack(Stack):
    if type(Stack) != CardStack:
        raise TypeError("Error: Object is not a Card Stack")
    else:
        return Stack.get_cards_on_stack()