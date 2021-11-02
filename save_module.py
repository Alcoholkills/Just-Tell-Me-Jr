import json

def read_data():
    with open("save.json", "r") as save:
        return json.load(save.readlines())

def write_data():
    return None

def add_data():
    return None

def remove_data():
    return None