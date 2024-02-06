from typing import List
from ..schema import MovingAverage, Event
from datetime import datetime, timedelta
from collections import deque

def calculate_moving_average(events: List[Event], window_size) -> List[MovingAverage]:
    """
    Calculate the moving average of delivery times for a list of events.

    This function calculates the moving average of delivery times for a list of events, 
    using a sliding window approach. The window size is specified in minutes.

    Args:
        events (List[Event]): A list of events. Each event is a dictionary that includes a timestamp and a delivery time.
        window_size (int): The size of the sliding window in minutes.

    Returns:
        List[MovingAverage]: A list of moving averages. Each moving average is a dictionary that includes a timestamp and an average delivery time.
    """
    window = deque()
    averages = []
    # Convert the timestamps to datetime objects and get the min and max
    timestamps = [datetime.strptime(event['timestamp'], '%Y-%m-%d %H:%M:%S.%f') for event in events if event['event_name'] == 'translation_delivered']

    if not timestamps:
        return []

    min_timestamp = min(timestamps)
    max_timestamp = max(timestamps)

    # Round down the min timestamp to the nearest minute
    min_timestamp = min_timestamp.replace(second=0, microsecond=0)

    # Round up the max timestamp to the nearest minute
    max_timestamp = max_timestamp + timedelta(minutes=1)

    # Initialize the current timestamp to the min timestamp
    current_timestamp = min_timestamp

    # Initialize the index for the events list
    i = 0

    # Iterate over every minute in the range of timestamps
    while current_timestamp <= max_timestamp:
        # Remove events from the window that are older than window_size minutes
        while window and current_timestamp - timestamps[i - len(window)] >= timedelta(minutes=window_size):
            window.popleft()

        # Add events to the window that are within the current minute
        while i < len(timestamps) and timestamps[i] <= current_timestamp:
            window.append(events[i]['duration'])
            i += 1

        # Calculate the average delivery time for the events in the window
        average_delivery_time = sum(window) / len(window) if window else 0

        # Add the result to the averages list
        averages.append(MovingAverage(date=current_timestamp.strftime('%Y-%m-%d %H:%M:%S'), average_delivery_time=average_delivery_time))

        # Move to the next minute
        current_timestamp += timedelta(minutes=1)


    return averages