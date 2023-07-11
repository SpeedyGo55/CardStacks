from CardStacks import CardStack
import random


def test_cardstack():
    stack = CardStack()
    assert str(stack) == "{'Spades': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], " \
                         "'Hearts': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], " \
                         "'Clubs': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace'], " \
                         "'Diamonds': ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']}"


def test_cardstack_in_play():
    stack = CardStack()
    assert str(
        stack.get_cards_in_play()) == "{'Spades': [], 'Hearts': [], 'Clubs': [], 'Diamonds': []}", "Cards in play is " \
                                                                                                   "not empty"


def test_cardstack_number_in_play():
    stack = CardStack()
    stack.draw(5)
    assert stack.number_of_cards_in_play() == 5, "Cards in play is not 5"
    rand = random.randint(1, 10)
    stack.draw(rand)
    assert stack.number_of_cards_in_play() == 5 + rand, f"Cards in play is not {5 + rand}"
    stack.draw(0)
    assert stack.number_of_cards_in_play() == 5 + rand, f"Cards in play is not {5 + rand}"


def test_cardstack_draw():
    stack = CardStack()
    drawn = stack.draw(5)
    assert len(drawn) == 5, "Drawn cards is not 5"
    rand = random.randint(1, 10)
    drawn = stack.draw(rand)
    assert len(drawn) == rand, f"Drawn cards is not {rand}"
    drawn = stack.draw(0)
    assert len(drawn) == 0, f"Drawn cards is not 0"


def test_cardstack_len():
    stack = CardStack()
    assert len(stack) == 52, "Stack length is not 52"
    stack.draw(5)
    assert len(stack) == 47, "Stack length is not 47"
    rand = random.randint(1, 10)
    stack.draw(rand)
    assert len(stack) == 47 - rand, f"Stack length is not {47 - rand}"
    stack = CardStack(suits=["Spades", "Hearts", "Clubs", "Diamonds"], ranks=["2", "3", "4", "5", "6", "7", "8", "9"])
    assert len(stack) == 32, "Stack length is not 32"
    stack.draw(5)
    assert len(stack) == 27, "Stack length is not 27"
    rand = random.randint(1, 10)
    stack.draw(rand)
    assert len(stack) == 27 - rand, f"Stack length is not {27 - rand}"