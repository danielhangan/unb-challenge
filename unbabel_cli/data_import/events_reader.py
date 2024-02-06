import json
from typing import Any, List

def process_events_json(file_name: str) -> List[Any]:
    """
    This function reads a JSON file and returns its contents as a list of objects.

    Args:
    file_name (str): The name of the JSON file to read.

    Returns:
    list: The contents of the JSON file as a list of objects.
    """

    # Check if the file name has the correct extension
    if not file_name.endswith('.json'):
        raise ValueError(f"File '{file_name}' is not a JSON file.")

    try:
        with open(file_name, 'r') as f:
            data = json.load(f)

        # Check if the data is a list
        if not isinstance(data, list):
            raise ValueError(f"File '{file_name}' does not contain a list of events as objects.")

        # Check if all elements in the list are dictionaries (i.e., objects)
        if not all(isinstance(item, dict) for item in data):
            raise ValueError(f"File '{file_name}' does not contain a list of events as objects.")

        return data

    except FileNotFoundError:
        raise FileNotFoundError(f"File '{file_name}' does not exist.")

    except json.JSONDecodeError:
        raise ValueError(f"File '{file_name}' is not a valid JSON file.")