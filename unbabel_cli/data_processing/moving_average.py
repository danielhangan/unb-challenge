from typing import List
from datetime import datetime
from ..schema import MovingAverage, Event


def aggregate_translation_delivered(data: List[Event], window_size: int) -> List[MovingAverage]:
    """
    This function calculates the moving average of 'translation_delivered' events.

    Args:
    data (list): List of events.
    window_size (int): The size of the moving window.

    Returns:
    list: A list of MovingAverage objects containing the date and average delivery time.
    """
    result = {}

    for event in data:
        if event['event_name'] == 'translation_delivered':
            minute = event['timestamp'][:16] + ':00'

            if minute not in result:
                result[minute] = {'count': 0, 'sum': 0}

            result[minute]['sum'] += event['duration']
            result[minute]['count'] += 1

    output = []
    
    for minute in sorted(result.keys()):
        average_delivery_time = result[minute]['sum'] / result[minute]['count']
        output.append(MovingAverage(date=datetime.strptime(minute, '%Y-%m-%d %H:%M:%S'), average_delivery_time=average_delivery_time))

    if len(output) > window_size:
        output.pop(0)

    return output