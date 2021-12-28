import enum
import json
import re
from util import formatedString
from util import boxString
from util import tableString
from deck import Deck
from card import Card

def main():
    """Entry point of the program"""
    pass

def help() -> None:
    """Prints all the help for the user"""
    return

def createNewDeck(hashList: list[int]) -> Deck:
    """Creates a new deck and returns it"""
    namm = input("<> Enter a deck name: ")[:50]
    if hash(namm.lower()) not in hashList:
        return Deck(namm)
    print("This name is already taken ; please chose another name.")
    createNewDeck(hashList)

def selectDeck(listDeck: list[Deck], show: bool = True) -> Deck:
    """Prints all the decks in table format and returns a deck given by user's input"""
    if show:
        viewDecks(listDeck)
    try:
        i = int(input("<> Enter a deck index: "))
    except ValueError:
        i = -1
    if i not in range(0, len(listDeck)):
        print("Please enter a valid deck number.")
        return selectDeck(listDeck, False)
    return listDeck[i]


def viewDecks(listDeck: list[Deck]) -> None:
    """Prints a table of all the deck ; index and deck name"""
    print(tableString(listDeck))

def viewCards(deck: Deck) -> None:
    """Prints all the cards contained in the given deck"""
    for index, card in enumerate(deck.deck):
        print(boxString(f"Card number: {index}")[:-1])
        print(card)

def viewCardMinimalist(deck: Deck) -> None:
    """Prints a table containing all cards in the given deck, in a minimalist way ; with card's name only"""
    print(tableString(deck.deck))
        

def createNewCard(deck: Deck) -> bool:
    """Creates a card with user's input and adds it to the deck given in parameters"""
    namm = input("<> Enter a card name: ")[:50]
    mess = input("<> (Optional) Enter a message: ")[:280]
    try:
        proba = float(input("<> (Optional) Enter a probability for this card: "))
    except ValueError:
        proba = 1
        print("Default probability.")
    return deck.addCard(Card(namm, mess, proba))

def removeDeck(deckList: list[Deck], show = True) -> None:
    """`removeDeck` shows the deck list and removes a deck from the list by the input of the user"""
    if show:
        viewDecks(deckList)
    try:
        i = int(input("<> Enter a deck index: "))
    except ValueError:
        i = -1
    if i not in range(0, len(deckList)):
        print("Please enter a valid deck index.")
        return selectDeck(deckList, False)
    deckList.pop(i)
    

def removeCard(deck: Deck, show = True) -> bool:
    """Prints all the cards in the given deck and removes one given user's input"""
    if show:
        viewCards(deck)
    try:
        i = int(input("<> Enter a card index"))
    except ValueError:
        i = -1
    if i not in range(0,len(deck.deck)):
        print("Please enter a valid deck index.")
        return selectDeck(deck, False)
    return deck.removeCard(deck.deck[i])
        

def saveDecks(listDeck: list[Deck]) -> None:
    """Saves the current deck list in `saveDecks.sav`"""
    with open("saveDecks.sav","w") as file:
        for deck in listDeck:
            file.write(deck.__repr__())

def loadDecks() -> list[Deck]:
    """Loads the `saveDecks.sav` into Python object `list[Deck]`"""
    returnedDeckList: list[Deck] = list()
    leverDeck: bool = False
    leverDraw: bool = False
    leverParent: bool = False
    leverChild: bool = False
    deckList: list[Card] = list()
    drawList: list[Card] = list()
    parentList: list = list()
    childList: list = list()
    with open("saveDecks.sav","r") as file:
        while True:
            line = file.readline()
            if not line:
                break
            if re.match(r"^\[\[.+\]\]$", line):
                namm = line[2:-2]
                continue
            if re.match(r"^Hash=", line):
                hass = int(line[5:])
                continue
            if re.match(r"^Size=", line):
                sizz = int(line[5:])
                continue
            if "[Deck]\n" == line:
                leverDeck = True
                continue
            if "[DrawingDeck]\n" == line:
                leverDeck = False
                leverDraw = True
                continue
            if "[isParent]\n" == line:
                leverDraw = False
                leverParent = True
                continue
            if "[isChild]\n" == line:
                leverParent = False
                leverChild = True
                continue
            if "\n" == line:
                leverChild = False
                tempDeck = Deck(namm)
                tempDeck.setDeck([Card(name=dic["Name"], message=dic["Message"], probability=dic["Proba"]) for dic in deckList])
                tempDeck.setDrawingDeck([Card(name=dic["Name"], message=dic["Message"], probability=dic["Proba"]) for dic in drawList])
                tempDeck.setIsParent([Card(name=dic["Name"], message=dic["Message"], probability=dic["Proba"]) for dic in parentList])
                tempDeck.setIsParent([Card(name=dic["Name"], message=dic["Message"], probability=dic["Proba"]) for dic in childList])
                returnedDeckList.append(tempDeck)
                continue
            if leverDeck:
                deckList.append(json.loads(line))
                continue
            if leverDraw:
                drawList.append(json.loads(line))
                continue
            if leverParent:
                parentList.append(json.loads(line))
                continue
            if leverChild:
                childList.append(json.loads(line))
                
                


if __name__ == "__main__":
    main()