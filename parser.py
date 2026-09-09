
import json

def load_logs(path):
    with open(path, "r") as file:
        return json.load(file)
