#!/usr/bin/env python3

import json
import click
from .data_import.events_reader import process_events_json
from .data_validation.events_validator import events_input_validator, events_output_validator
from .data_processing.moving_average import aggregate_translation_delivered

@click.command()
@click.option('--input_file', default='events.json', type=str, help='Input file name.')
@click.option('--window_size', default=10, type=click.IntRange(10, 25), help='Window size for the moving average (between 10 and 25).')
def main(input_file, window_size):
    """
    Main function that reads the input file and prints the moving average of 'translation_delivered' events.
    """

    # Load the data from the input file
    data = process_events_json(input_file)

    # validate input data
    events_input_validator(data)

    # Calculate the moving average
    result = aggregate_translation_delivered(data, window_size)
    
    # validate return output
    events_output_validator(result)
    
    print(json.dumps([item.model_dump() for item in result], default=str, indent=2))


if __name__ == '__main__':
    main()