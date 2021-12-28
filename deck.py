import random
from numpy import cumsum
from util import formatedString
from card import Card


class Deck:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self.hash: int = hash(name.lower())
        self.size: int = 0
        self.deck: list[Card] = list()
        self.drawingDeck: list[Card] = list()
        self.isParent: list[str] = list()
        self.isChild: list[str] = list()
    
    def setDeck(self, listDeck: list[Card]) -> None:
        self.deck = listDeck
        self.updateSize()
    
    def setDrawingDeck(self, listDraw: list[Card]) -> None:
        self.drawingDeck = listDraw
    
    def setIsParent(self, listParent: list[str]) -> None:
        self.isParent = listParent
    
    def setIsChild(self, listChild: list[str]) -> None:
        self.isChild = listChild
        

    def hashDeck(self) -> list[str]:
        """`hashDeck` returns a list of all the cards as their hash"""
        return [xcard.hash for xcard in self.deck]

    def addCard(self, card: Card) -> bool:
        """`addCard` adds a card to the Deck and returns True if successful, else False"""
        if card.hash in self.hashDeck() or not isinstance(card, Card):
            return False
        self.deck.append(card)
        self.updateSize()
        self.addCardDrawingDeck(card)
        return True

    def removeCard(self, card: Card) -> bool:
        """`removeCard` removes a card from the Deck and returns True if successful, else False"""
        if card.hash not in self.hashDeck() or not isinstance(card, Card):
            return False
        for index, xcard in enumerate(self.deck):
            if card.hash == xcard.hash:
                self.deck.pop(index)
                self.updateSize()
                self.removeCardDrawingDeck(card)
                return True

    def updateSize(self) -> None:
        """`updateSize` updates the `self.size` of the Deck"""
        self.size = len(self.deck)

    def viewCards(self) -> None:
        """`viewCards` prints to the stdout all the cards"""
        for card in self.deck:
            print(card)

    def removeCardDrawingDeck(self, card: Card) -> None:
        for index, cardDeck in self.drawingDeck:
            if cardDeck.hash == card.hash:
                self.drawingDeck.pop(index)

    def addCardDrawingDeck(self, card: Card) -> None:
        self.drawingDeck.append(card)

    def draw(self) -> Card:
        """Draws a card from the deck"""
        if not self.drawingDeck:
            self.drawingDeck = self.deck[:]
        tempList: list[float] = [c.proba for c in self.drawingDeck]
        bggst: int = sum(tempList)
        cumList = list(map(lambda x: x / bggst, list(cumsum([0.0] + tempList))))
        tirage = random.random()
        for i in range(len(cumList) - 1):
            if cumList[i] <= tirage and tirage < cumList[i + 1]:
                return self.drawingDeck.pop(i)
        return self.drawingDeck.pop()

    def __repr__(self) -> str:
        namm = f"[[{self.name}]]\n"
        hass = f"Hash={self.hash}\n"
        sizz = f"Size={self.size}\n"
        decc = "[Deck]\n"
        for crd in self.deck:
            decc += str(crd.__repr__()) + "\n"
        drww = "[DrawingDeck]\n"
        for crd in self.drawingDeck:
            drww += str(crd.__repr__()) + "\n"
        isPr = "[isParent]\n"
        for crd in self.isParent:
            isPr += str(crd.__repr__()) + "\n"
        isCh = "[isChild]\n"
        for crd in self.isChild:
            isCh += str(crd.__repr__()) + "\n"
        return namm + hass + sizz + decc + drww + isPr + isCh
        
        
    
    def __str__(self):
        temp: str = ""
        namm: str = formatedString(self.name, "| *")
        sizz: str = formatedString(f"Size: {self.size}", "| |")
        parr: str = formatedString(f"Parent: {bool(self.isParent)}", "| |")
        chld: str = formatedString(f"Child: {bool(self.isChild)}", "| |")
        temp += "  +-------------------------+\n"
        temp += " /                         /|\n"
        temp += "+-------------------------+ |\n"
        temp += "|                         | |\n"
        temp += "{:^25}".format(namm)
        temp += "|                         |/|\n"
        temp += "*---*                 *---* |\n"
        temp += "|    \_______________/    | |\n"
        temp += "|                         | |\n"
        temp += f"{sizz:^25}"
        temp += f"{parr:^25}"
        temp += f"{chld:^25}"
        temp += "|                         | +\n"
        temp += "|                         |/\n"
        temp += "+-------------------------+\n"
        return temp


if __name__ == "__main__":
    d = Deck("Fire")
    print(d.name)
    print(d.size)
    c1 = Card("Domir", "La il commence a etre vraiment tard")
    c2 = Card("Jouer a SkullGirls", "Mais c'est vrai que t'as pas joue aujourd'hui")
    c3 = Card("Faire du sport", "C'est OK ;)")
    d.addCard(c1)
    d.addCard(c2)
    d.addCard(c3)
    d.viewCards()
    print(d)
    print(d.draw())
    print(d.draw())
    print(d.draw())
    print(d.draw())
    print(d.__repr__())
