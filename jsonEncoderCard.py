import json
from card import Card

class CardEncoder(json.JSONEncoder):
    def default(self, card: Card) -> dict:
        if isinstance(card, Card):
            return card.__dict__()
        return json.JSONEncoder.default(self, card)

if __name__ == "__main__":
    a = json.dumps(Card("Test"), cls=CardEncoder)
    print(type(a))
    print(a)
    b = json.loads(a)
    print(type(b))
    print(b["Name"])