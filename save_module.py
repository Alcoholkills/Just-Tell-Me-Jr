import json, os, traceback


def read_data() -> list:
    """
    Reads data from the save file as a python object : list of dict
    """
    with open("save.json", "r") as save:
        return json.load(save)


def write_data(new_save: list) -> bool:
    """
    Writes data to the save file as a json format
    
    `new_save` is the data that needs to be saved
    """
    try:
        with open("new_save.json", "w") as new_save_file:
            json.dump(new_save, new_save_file, indent=4)
        os.rename("new_save.json", "save.json")
        return True
    except Exception:
        print(traceback.format_exc())
        return False
  
    
def add_data(save: list, item: dict) -> list:
    """
    Adds `item` to the saved list `save`
    
    This function returns the update `save`
    """
    try:
        save.append(item)
        return save
    except Exception:
        print(traceback.format_exc())
        return save


def remove_data(save: list, a_hash: int) -> bool:
    """
    Removes `item` from the save list `save`
    """
    try:
        for item in save:
            if item["Hash"] == a_hash:
                save.remove(item)
                return True
    except Exception:
        print(traceback.format_exc())
        return False


def create_item() -> dict:
    """
    Creates an empty item
    
    It creates the template for the items used in the app
    
    `{"Name":"","Hash":0,"Probability":0,"SubActivities":[],"Notes":""}`
    """
    return {"Name":"","Hash":0,"Probability":0,"SubActivities":[],"Notes":""}


def edit_name(item: dict, name: str) -> dict:
    """
    Writes over the `item["Name"]` and `item["Hash"]` with the provided `name` and returns the `item`
    """
    item["Name"] = name
    item["Hash"] = hash(name)
    return item


def edit_probability(item: dict, proba: float) -> dict:
    """
    Writes over the `item["Probability"]` with the provided `probability` and returns the `item`
    """
    item["Probability"] = proba
    return item


def edit_notes(item: dict, new_note: str) -> dict:
    """
    Writes over the `item["Notes"]` with the provided `new_notes` and returns the `item`
    """
    item["Notes"] = new_note
    return item

def add_subactivity(item: dict, activity: dict) -> dict:
    """
    Adds an `item` to the `item["SubActivities"]` list
    """
    item["SubActivities"].append(activity)
    return item

def remove_subactivity(item: dict, a_hash: int) -> dict:
    """
    Removes an `item` from the `item["SubActivities"]` list
    """
    for sub_item in item["SubActivities"]:
        if sub_item["Hash"] == a_hash:
            item["SubActivities"].remove(sub_item)
            return item

if __name__ == "__main__":
    pass