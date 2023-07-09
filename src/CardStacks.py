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

    def __len__(self):
        count = 0
        for suit in self.cards_on_stack:
            count += len(self.cards_on_stack[suit])
        return count

    def get_cards_in_play(self):
        return self.cards_in_play

    def get_cards_on_stack(self):
        return self.cards_on_stack

    def number_of_cards_in_play(self):
        count = 0
        for suit in self.cards_in_play:
            count += len(self.cards_in_play[suit])
        return count

    def draw(self, amount):
        output = []
        if amount > 52 or amount < 0:
            raise ValueError("Error: Amount is not between 0 and 52")
        if amount > len(self):
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

    def put_card_back(self, card):
        if type(card) != tuple:
            raise TypeError("Error: Card is not a tuple")
        if len(card) != 2:
            raise ValueError("Error: Card tuple does not have 2 values")
        if card[0] not in self.cards_in_play:
            raise ValueError("Error: Suit is not valid")
        if card[1] not in self.cards_in_play[card[0]]:
            raise ValueError("Error: Card is not valid")
        self.cards_on_stack[card[0]].append(card[1])
        self.cards_in_play[card[0]].remove(card[1])
        return True

    def put_hand_back(self, hand):
        if type(hand) != list:
            raise TypeError("Error: Hand is not a list")
        for card in hand:
            self.put_card_back(card)
        return True

    def remove_card_from_stack(self, card):
        if type(card) != tuple:
            raise TypeError("Error: Card is not a tuple")
        if len(card) != 2:
            raise ValueError("Error: Card tuple does not have 2 values")
        if card[0] not in self.cards_on_stack:
            raise ValueError("Error: Suit is not valid")
        if card[1] not in self.cards_on_stack[card[0]]:
            raise ValueError("Error: Card is not valid")
        self.cards_on_stack[card[0]].remove(card[1])
        return True

    def remove_cards_from_stack(self, cards):
        if type(cards) != list:
            raise TypeError("Error: Cards is not a list")
        for card in cards:
            self.remove_card_from_stack(card)
        return True

    def delete_suit(self, suit):
        if type(suit) != str:
            raise TypeError("Error: Suit is not a string")
        if suit not in self.cards_on_stack or suit not in self.cards_in_play:
            raise ValueError("Error: Suit is not valid")
        del self.cards_on_stack[suit]
        del self.cards_in_play[suit]
        return True

    def delete_suits(self, suits):
        if type(suits) != list:
            raise TypeError("Error: Suits is not a list")
        for suit in suits:
            self.delete_suit(suit)
        return True

    def delete_rank(self, rank):
        if type(rank) != str:
            raise TypeError("Error: Rank is not a string")
        for suit in self.cards_on_stack:
            if rank in self.cards_on_stack[suit]:
                self.cards_on_stack[suit].remove(rank)
        for suit in self.cards_in_play:
            if rank in self.cards_in_play[suit]:
                self.cards_in_play[suit].remove(rank)
        return True

    def add_suit(self, suit):
        if type(suit) != str:
            raise TypeError("Error: Suit is not a string")
        if suit in self.cards_on_stack:
            raise ValueError("Error: Suit is already in stack")
        self.cards_in_play[suit] = []
        self.cards_on_stack[suit] = []
        return True

    def add_rank(self, rank):
        if type(rank) != str:
            raise TypeError("Error: Rank is not a string")
        for suit in self.cards_on_stack:
            if rank not in self.cards_on_stack[suit]:
                self.cards_on_stack[suit].append(rank)
        for suit in self.cards_in_play:
            if rank not in self.cards_in_play[suit]:
                self.cards_in_play[suit].append(rank)
        return True




def get_cards_in_play(stack):
    if type(stack) != CardStack:
        raise TypeError("Error: Object is not a Card Stack")
    else:
        return stack.get_cards_in_play()


def get_cards_on_stack(stack):
    if type(stack) != CardStack:
        raise TypeError("Error: Object is not a Card Stack")
    else:
        return stack.get_cards_on_stack()
