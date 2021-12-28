import random
from card import Card


class Deck:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hash: int = hash(name)
        self.size: int = 0
        self.deck: list[Card] = list()
        self.isParent: bool = False
        self.isChild: bool = False

    def hashDeck(self) -> list[str]:
        """`hashDeck` returns a list of all the cards as their hash"""
        return [xcard.hash for xcard in self.deck]

    def addCard(self, card: Card) -> bool:
        """`addCard` adds a card to the Deck and returns True if successful, else False"""
        if card.hash in self.hashDeck() or not isinstance(card, Card):
            return False
        self.deck.append(card)
        self.updateSize()
        return True

    def removeCard(self, card: Card) -> bool:
        """`removeCard` removes a card from the Deck and returns True if successful, else False"""
        if card.hash not in self.hashDeck() or not isinstance(card, Card):
            return False
        for index, xcard in enumerate(self.deck):
            if card.hash == xcard.hash:
                self.deck.pop(index)
                self.updateSize()
                return True

    def updateSize(self) -> None:
        """`updateSize` updates the `self.size` of the Deck"""
        self.size = len(self.deck)

    def viewCards(self) -> None:
        """`viewCards` prints to the stdout all the cards"""
        # TODO
        pass

    def draw(self) -> Card:
        return random.choice(self.deck)


if __name__ == "__main__":
    d = Deck("Fire")
    print(d.name)
    print(d.size)
