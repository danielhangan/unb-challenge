

import random
from datetime import datetime, timedelta

languages = ["en", "fr", "de", "es", "it"]
clients = ["airliberty", "taxi-eats", "hotel-paradise", "fast-delivery", "book-club"]
events_names = ["translation_delivered", "translation_started", "translation_failed"]

start_time = datetime.strptime("2018-12-26 18:11:08.509654", "%Y-%m-%d %H:%M:%S.%f")

def generate_json_data():
    events =[]
    for i in range(100):
        event_time = start_time + timedelta(minutes=i//5, seconds=i%5*12)
        event = {
            "timestamp": event_time.strftime("%Y-%m-%d %H:%M:%S.%f"),
            "translation_id": f"5aa5b2f39f7254a75a{i:02}",
            "source_language": random.choice(languages),
            "target_language": random.choice(languages),
            "client_name": random.choice(clients),
            "event_name": random.choice(events_names),
            "nr_words": random.randint(10, 100),
            "duration": random.randint(10, 60)
        }
        events.append(event)
    return events
    