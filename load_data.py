import json

FILE_PATH = "ships_data.json"


def load_data():
  """ Loads a JSON file """
  with open(FILE_PATH, "r", encoding="utf-8") as handle:
    return json.load(handle)
