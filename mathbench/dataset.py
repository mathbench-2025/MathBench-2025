import json

def load_dataset(path):
    with open(path, "r") as f:
        data = json.load(f)
    return data
