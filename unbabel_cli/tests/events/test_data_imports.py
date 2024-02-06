import os
import json
import pytest
from typing import List
from generate_test_data import generate_json_data

from unbabel_cli.data_import.events_reader import process_events_json



@pytest.fixture
def test_file_name():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Construct the path to the test_events.json file
    test_file_dir = os.path.join(current_dir, 'test_data')
    os.makedirs(test_file_dir, exist_ok=True)  # Create the directory if it doesn't exist
    
    test_good_data_file_path = os.path.join(test_file_dir, 'events_good_data.json')
    # check if file already exists
    if not os.path.exists(test_good_data_file_path):
        # Create a test JSON file with a list of objects
        good_data = generate_json_data()
        
        # write to test_file_path
        with open(test_good_data_file_path, 'w') as f:
            json.dump(good_data, f)

    yield test_good_data_file_path

    # Clean up the test file
    os.remove(test_good_data_file_path)


def test_process_events_json(test_file_name):
    # Test that the function returns the correct data
    data = process_events_json(test_file_name)
    # assert if data is a list of objects
    assert isinstance(data, List)

def test_process_events_json_invalid_file():
    # Test that the function raises an exception for an invalid file
    with pytest.raises(ValueError):
        process_events_json('test.txt')

def test_process_events_json_nonexistent_file():
    # Test that the function raises an exception for a nonexistent file
    with pytest.raises(FileNotFoundError):
        process_events_json('nonexistent.json')

def test_process_events_json_invalid_json(test_file_name):
    # Test that the function raises an exception for an invalid JSON file
    with open(test_file_name, 'w') as f:
        f.write('invalid json')
    with pytest.raises(ValueError):
        process_events_json(test_file_name)

def test_process_events_json_not_list(test_file_name):
    # Test that the function raises an exception for a JSON file that does not contain a list
    with open(test_file_name, 'w') as f:
        json.dump({'event_name': 'test_event', 'timestamp': '2022-01-01T00:00:00Z'}, f)
    with pytest.raises(ValueError):
        process_events_json(test_file_name)