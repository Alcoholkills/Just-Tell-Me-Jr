s = set()

def str_card(card, num_tab: int) -> str:
    tab = "\t" * num_tab
    tab_minus_one = "\t" * (num_tab - 1)
    card_subActivites = card.get_subActivities()
    str_return = ""
    if card_subActivites != list():
        for sub_card in card_subActivites:
            str_return += str_card(sub_card, num_tab + 1)
    else :
        str_return = "[]"
    return f"[\n{tab}{card.Name}\n{tab}{card.Hash}\n{tab}{card.Probability}\n{tab}{str_return}\n{tab}{card.Notes}\n{tab_minus_one}]"

def rep_card(card, num_tab: int) -> str:
    tab = "\t" * num_tab
    tab_minus_one = "\t" * (num_tab - 1)
    card_subActivites = card.get_subActivities()
    str_return = ""
    if card_subActivites != list():
        for sub_card in card_subActivites:
            str_return += rep_card(sub_card, num_tab + 1)
    else :
        str_return = "[]"
    return f"[\n{tab}Name: {card.Name}\n{tab}Hash: {card.Hash}\n{tab}Probability: {card.Probability}\n{tab}SubActivites: {str_return}\n{tab}Notes: {card.Notes}\n{tab_minus_one}]"

def dico_card(card) -> dict:
    dico = dict()
    subAct = list()
    dico["Name"]=card.get_name()
    dico["Hash"]=card.get_hash()
    dico["Probability"]=card.get_probability()
    if card.get_subActivities() == list():
        dico["SubActivities"]=card.get_subActivities()
    else:
        for sub_card in card.get_subActivities():
            subAct.append(dico_card(sub_card))
        dico["SubActivities"]=subAct
    dico["Notes"]=card.get_notes()
    return dico

def find_all_hash(card) -> list:
    l = [card.get_hash()]
    l
    if card.get_subActivities() != list():
        for sub_card in card.get_subActivities():
            l += find_all_hash(sub_card)
    return l

def explore_and_delete(parent_card, card, hash_to_delete):
    if card.get_hash() == hash_to_delete:
        parent_card.remove_subActivities(card)
        return
    for sub_card in card.get_subActivities():
        explore_and_delete(card, sub_card, hash_to_delete)

def explore_and_add(parent_card, new_card, parent_hash_):
    s.add((parent_card.get_hash(), parent_hash_))
    if parent_card.get_hash() == parent_hash_:
        parent_card.add_subActivities(new_card)
        return
    elif parent_card in find_all_hash(parent_card):
        for sub_card in parent_card.get_subActivities():
            explore_and_add(sub_card, new_card, parent_hash_)

class Card():
    def __init__(self,
                 name: str = "name",
                 hash_: int = 0,
                 probability: float = 0,
                 subActivities: list = [],
                 notes: str = "notes") -> None:
        self.Name: str = name
        self.Hash: int = hash_
        self.Probability: float = probability
        self.SubActivities: list[Card] = subActivities
        self.Notes: str = notes
    
    def __str__(self) -> str:
        return str_card(self, 1)
        # temp = "[\n\t"
        # for card in self.SubActivities:
        #     temp += str(card)
        # return f"[\n\t{self.Name}\n\t{self.Hash}\n\t{self.Probability}\n\t{self.SubActivities}\n\t{self.Notes}\n]"

    def __repr__(self) -> str:
        return rep_card(self, 1)
    
    def __dict__(self) -> dict:
        return dico_card(self)

    def get_name(self):
        return self.Name
    
    def set_name(self, name):
        self.Name = name
    
    def get_hash(self):
        return self.Hash
    
    def set_hash(self, hash):
        self.Hash = hash
    
    def get_probability(self):
        return self.Probability
    
    def set_probability(self, probability):
        self.Probability = probability
        
    def get_subActivities(self):
        return self.SubActivities
    
    def set_subActivities(self, subActivities):
        self.SubActivities = subActivities
    
    def add_subActivities(self, card):
        self.SubActivities.append(card)
    
    def add_a_subActivities(self, new_card, parent_card_hash):
        if parent_card_hash in find_all_hash(self):
            if self.get_hash() == parent_card_hash:
                self.add_subActivities(new_card)
                return
            else:
                for sub_card in self.get_subActivities():
                    explore_and_add(sub_card, new_card, parent_card_hash)
    
    def remove_subActivities(self, card):
        self.SubActivities.remove(card)
    
    def remove_a_subActivities(self, card):
        card_to_remove_hash = card.get_hash()
        if card_to_remove_hash in find_all_hash(self):
            if self.get_hash() == card_to_remove_hash:
                del self
                return
            for sub_card in self.get_subActivities():
                explore_and_delete(self, sub_card, card_to_remove_hash)
        else:
            print("Error in remove_subActivities")
        
    def get_notes(self):
        return self.Notes
    
    def set_notes(self, notes):
        self.Notes = notes
    
if __name__ == "__main__":
    b = Card(name="b")
    c = Card(name="c")
    d = Card(name="d",subActivities=[c,b])
    # print(c)
    print(d)
    c = Card(name="c", subActivities=[b])
    d = Card(name="d", subActivities=[c])
    print(d)
    print(rep_card(d, 1))
    print(dico_card(b))
    print(dico_card(d))
    b = Card(name="b",hash_=-33)
    c = Card(name="c",hash_=4532)
    d = Card(name="d",hash_=1,subActivities=[c,b])
    # print(find_all_hash(d))
    d.remove_subActivities(b)
    print("'-'-"*5)
    print(d)
    """
    Ne fonctionne pas
    d.remove_subActivities(d)
    print(d)
    """
    b = Card(name="b",hash_=-33)
    c = Card(name="c",hash_=4532)
    d = Card(name="d",hash_=1)
    print(d)
    print("'-'-"*5)
    d.add_a_subActivities(c, d.get_hash())
    print(c)