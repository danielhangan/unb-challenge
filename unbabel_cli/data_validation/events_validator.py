from pydantic import ValidationError
from typing import List
from ..schema import Event, MovingAverage

def events_input_validator(data_list: List[dict]):
    for data in data_list:
        try:
            Event(**data)
        except ValidationError as e:
            raise ValueError(f"Data input validation error: {e}")


def events_output_validator(output: List[MovingAverage]):
    if not isinstance(output, list):
        raise TypeError("Output should be a list")
    for item in output:
        if not isinstance(item, MovingAverage):
            raise TypeError("Each item in the output should be an instance of MovingAverage")