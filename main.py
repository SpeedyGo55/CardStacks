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
