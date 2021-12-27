from card import Card


class Deck:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hash: int = hash(name)
        self.size: int = 0
        self.isParent: bool = False
        self.isChild: bool = False
        self.deck: list[Card] = list()

    def hashDeck(self) -> list[str]:
        """`hashDeck` returns a list of all the cards as their hash"""
        return [xcard.hash for xcard in self.deck]

    def addCard(self, card: Card) -> bool:
        if 


if __name__ == "__main__":
    d = Deck("Fire")
    print(d.name)
    print(d.size)
