
# PythonCardStacks

---

## Description

PythonCards is a Python library for creating playing cards and playing card stacks. It is designed to be extensible and easy to use.

## Installation

```bash
pip install CardStacks
```

## Usage

This is an Example showing how to create a deck of cards and draw a hand of 5 cards.
```python
from CardStacks import CardStack

Stack = CardStack()
hand = Stack.draw(5)
print(hand)
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[GNU GPLv3](https://choosealicense.com/licenses/gpl-3.0/)