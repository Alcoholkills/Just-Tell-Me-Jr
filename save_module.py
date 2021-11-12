import card, json

# TODO
# Let's only make 1 level deep cards for now
# Add multi level later
class Save():
    def __init__(self, list_of_cards: list[card.Card] = None) -> None:
        if list_of_cards is None:
            list_of_cards = []
        self.List_of_Cards = list_of_cards
    
    def __str__(self) -> str:
        s = "[\n"
        for each_card in self.get_list_of_cards():
            s += card.str_card(each_card, 2)
        s += "\n]"
        return s
    
    def save_Save(self) -> None:
        with open("save.json", "w") as file:
            json.dump(self.convert_to_python_object(),file,indent=4)
    
    def convert_to_python_object(self):
        l = list()
        for card in self.get_list_of_cards():
            l.append(card.__dict__())
        return l
    
    def load_Save(self) -> None:
        with open("save.json", "r") as file:
            json.load(file)
    
    def get_list_of_cards(self) -> list[card.Card]:
        return self.List_of_Cards

    def set_list_of_cards(self, list_of_cards: list) -> None:
        self.List_of_Cards = list_of_cards
    
    def add_card(self, new_card: card.Card) -> None:
        self.List_of_Cards.append(new_card)
    
    def add_card_from_parent_card(self, new_card: card.Card, parent_card: card.Card) -> None:
        parent_hash = parent_card.get_hash()
        self.add_card_from_parent_hash(self, new_card, parent_hash)
    
    def add_card_from_parent_hash(self, new_card: card.Card, parent_hash: int) -> bool:
        if parent_hash in self.find_all_hash():
            for cards in self.get_list_of_cards():
                if parent_hash in card.find_all_hash(cards):
                    cards.add_a_subActivities(new_card, parent_hash)
                    return True
        else:
            return False
    
    def remove_card_by_card(self, card_to_remove: card.Card) -> None:
        self.List_of_Cards.remove(card_to_remove)
    
    def remove_card_by_hash(self, hash_to_remove: int) -> None:
        for card in self.get_list_of_cards():
            if card.get_hash() == hash_to_remove:
                self.remove_card_by_card(card)
    
    def find_all_hash(self) -> list:
        l = list()
        for cards in self.get_list_of_cards():
            l += card.find_all_hash(cards)
        return l

if __name__ == "__main__":
    s = Save()
    s.add_card(card.Card(name="Jouer a un jeu video", hash_=10001))
    s.add_card(card.Card(name="Travailler", hash_=321432))
    print(s)
    s.save_Save()
    a = card.Card(name="a",hash_=1)
    b = card.Card(name="b",hash_=2)
    c = card.Card(name="a",hash_=1)
    print(a == b)
    print(a == a)
    print(a == c)
    
    # TODO
    # For later development
    # def remove_card(self, hash_to_remove: int) -> None:
    #     parent_card = None
    #     if hash_to_remove in self.explore_fetch_hash():
    #         for card in self.get_list_of_cards():
    #             parent_card = card
    #             if hash_to_remove == card.get_hash():
    #                 pass
        
    # def explore_fetch_hash(self):
    #     l = list()
    #     for card in self.get_list_of_cards():
    #         l.append(card.get_hash())
    #         if card.get_subActivities() != list():
    #             for sub_card in card.get_subActivities():
    #                 l += find_all_hash(sub_card)
    #         return l
        


















# import json, os, traceback


# def read_data() -> list:
#     """
#     Reads data from the save file as a python object : list of dict
#     """
#     with open("save.json", "r") as save:
#         return json.load(save)


# def write_data(new_save: list) -> bool:
#     """
#     Writes data to the save file as a json format
    
#     `new_save` is the data that needs to be saved
#     """
#     try:
#         with open("new_save.json", "w") as new_save_file:
#             json.dump(new_save, new_save_file, indent=4)
#         os.rename("new_save.json", "save.json")
#         return True
#     except Exception:
#         print(traceback.format_exc())
#         return False
  
    
# def add_item(save: list, item: dict) -> list:
#     """
#     Adds `item` to the saved list `save`
    
#     This function returns the update `save`
#     """
#     try:
#         save.append(item)
#         return save
#     except Exception:
#         print(traceback.format_exc())
#         return save


# def remove_item(save: list, a_hash: int) -> bool:
#     """
#     Removes `item` from the save list `save`
#     """
#     try:
#         for item in save:
#             if item["Hash"] == a_hash:
#                 save.remove(item)
#                 return True
#     except Exception:
#         print(traceback.format_exc())
#         return False

# def create_item() -> dict:
#     """
#     Creates an empty item
    
#     It creates the template for the items used in the app
    
#     `{"Name":"","Hash":0,"Probability":0,"SubActivities":[],"Notes":""}`
#     """
#     return {"Name":"","Hash":0,"Probability":0,"SubActivities":[],"Notes":""}

# def modify_item(save: list)

# def edit_name(item: dict, name: str) -> dict:
#     """
#     Writes over the `item["Name"]` and `item["Hash"]` with the provided `name` and returns the `item`
#     """
#     item["Name"] = name
#     item["Hash"] = hash(name)
#     return item


# def edit_probability(item: dict, proba: float) -> dict:
#     """
#     Writes over the `item["Probability"]` with the provided `probability` and returns the `item`
#     """
#     item["Probability"] = proba
#     return item


# def edit_notes(item: dict, new_note: str) -> dict:
#     """
#     Writes over the `item["Notes"]` with the provided `new_notes` and returns the `item`
#     """
#     item["Notes"] = new_note
#     return item

# def add_subactivity(item: dict, activity: dict) -> dict:
#     """
#     Adds an `item` to the `item["SubActivities"]` list
#     """
#     item["SubActivities"].append(activity)
#     return item

# def remove_subactivity(item: dict, a_hash: int) -> dict:
#     """
#     Removes an `item` from the `item["SubActivities"]` list
#     """
#     for sub_item in item["SubActivities"]:
#         if sub_item["Hash"] == a_hash:
#             item["SubActivities"].remove(sub_item)
#             return item

# if __name__ == "__main__":
#     pass