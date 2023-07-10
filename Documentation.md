
# Documentation

---

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Introduction](#introduction)
- [Functions in Detail](#functions-in-detail)
  - [CardStack](#cardstack)
  - [CardStack.draw(amount)](#cardstackdrawamount)
  - [CardStack.draw_stack(amount)](#cardstackdraw_stackamount)
  - [len(CardStack)](#lencardstack)
  - [CardStack.number_of_cards_in_play()](#cardstacknumber_of_cards_in_play)
  - [CardStack.put_card_back(card)](#cardstackput_card_backcard)
  - [CardStack.put_cards_back(cards)](#cardstackput_cards_backcards)
  - [CardStack.put_hand_back(hand)](#cardstackput_hand_backhand)
  - [CardStack.remove_card_from_stack(card)](#cardstackremove_card_from_stackcard)
  - [CardStack.remove_cards_from_stack(cards)](#cardstackremove_cards_from_stackcards)
  - [CardStack.delete_suit(suit)](#cardstackdelete_suitsuit)
  - [CardStack.delete_rank(rank)](#cardstackdelete_rankrank)
  - [CardStack.delete_suits(suits)](#cardstackdelete_suitssuits)
  - [CardStack.delete_ranks(ranks)](#cardstackdelete_ranksranks)
  - [CardStack.add_suit(suit)](#cardstackadd_suitsuit)
  - [CardStack.add_rank(rank)](#cardstackadd_rankrank)
  - [CardStack.add_suits(suits)](#cardstackadd_suitssuits)
  - [CardStack.add_ranks(ranks)](#cardstackadd_ranksranks)
  - [CardStack.get_cards_in_play()](#cardstackget_cards_in_play)
  - [CardStack.get_cards_on_stack()](#cardstackget_cards_on_stack)
  - [get_cards_in_play(CardStack)](#get_cards_in_playcardstack)
  - [get_cards_on_stack(CardStack)](#get_cards_on_stackcardstack)

## Introduction

This is a Simple Example in which a Default CardStack is created and a hand of 5 cards is drawn from it, which is then printed to the console.

```python
from CardStacks import CardStack

Stack = CardStack()
hand = Stack.draw(5)
print(hand)
```

## Functions in Detail

### CardStack

```python
CardStack(suits, ranks)
```
This is the main class of the library. It is used to create a CardStack object, which is a stack of cards. It can be used to create a deck of cards, a hand of cards, or any other stack of cards.

Per default, the CardStack is initialized with the standard 52 cards of a deck. The suits and ranks can be changed by passing a list of suits and ranks to the constructor.

### CardStack.draw(amount)

```python
CardStack.draw(amount)
```
This function is used to draw a certain amount of cards from the stack. It returns a list of cards. The single Cards are represented as Tuple of the form (Suit, Rank).

### CardStack.draw_stack(amount)

```python
CardStack.draw_stack(amount)
```
This function is used to draw a certain amount of cards from the stack. It returns a Dictionary containing the drawn cards.

The Dictionary is of the form {Suit: Ranks, ...}, where the Ranks are a list of the ranks of the cards of the respective suit.

### len(CardStack)

```python
len(CardStack)
```
This function returns the amount of cards remaining on the stack.

### CardStack.number_of_cards_in_play()

```python
CardStack.number_of_cards_in_play()
```
This function returns the amount of cards that have been drawn from the stack.

### CardStack.put_card_back(card)

```python
CardStack.put_card_back(card)
```
This function puts a card back on the stack. The card has to be passed as a Tuple of the form (Suit, Rank).

### CardStack.put_cards_back(cards)

```python
CardStack.put_cards_back(cards)
```
This function puts a list of cards back on the stack. The cards have to be passed as a list of Tuples of the form (Suit, Rank).

### CardStack.put_hand_back(hand)

```python
CardStack.put_hand_back(hand)
```
This function puts a hand of cards back on the stack. The hand has to be passed as a List of Tuples of the form (Suit, Rank).

### CardStack.remove_card_from_stack(card)

```python
CardStack.remove_card_from_stack(card)
```
This function removes a card from the stack. The card has to be passed as a Tuple of the form (Suit, Rank).

### CardStack.remove_cards_from_stack(cards)

```python
CardStack.remove_cards_from_stack(cards)
```
This function removes a list of cards from the stack. The cards have to be passed as a list of Tuples of the form (Suit, Rank).

### CardStack.delete_suit(suit)

```python
CardStack.delete_suit(suit)
```
This function deletes all cards of a certain suit and the suit from the stack. The suit has to be passed as a String.

### CardStack.delete_rank(rank)

```python
CardStack.delete_rank(rank)
```
This function deletes the rank in all suits from the stack. The rank has to be passed as a String.

### CardStack.delete_suits(suits)

```python
CardStack.delete_suits(suits)
```
This function deletes all cards of a list of suits and the suits from the stack. The suits have to be passed as a list of Strings.

### CardStack.delete_ranks(ranks)

```python
CardStack.delete_ranks(ranks)
```
This function deletes the ranks in all suits from the stack. The ranks have to be passed as a list of Strings.

### CardStack.add_suit(suit)

```python
CardStack.add_suit(suit)
```
This function adds an empty suit to the stack. The suit has to be passed as a String.

### CardStack.add_rank(rank)

```python
CardStack.add_rank(rank)
```
This function adds a rank to all suits in the stack. The rank has to be passed as a String.

### CardStack.add_suits(suits)

```python
CardStack.add_suits(suits)
```
This function adds a list of empty suits to the stack. The suits have to be passed as a list of Strings.

### CardStack.add_ranks(ranks)

```python
CardStack.add_ranks(ranks)
```
This function adds a list of ranks to all suits in the stack. The ranks have to be passed as a list of Strings.

### CardStack.get_cards_in_play()

```python
CardStack.get_cards_in_play()
```
This function returns a list of all cards that have been drawn from the stack.

### CardStack.get_cards_on_stack()

```python
CardStack.get_cards_on_stack()
```
This function returns a list of all cards that are still on the stack.

### get_cards_in_play(CardStack)

```python
get_cards_in_play(CardStack)
```
This function returns a list of all cards that have been drawn from the stack.

### get_cards_on_stack(CardStack)

```python
get_cards_on_stack(CardStack)
```
This function returns a list of all cards that are still on the stack.
