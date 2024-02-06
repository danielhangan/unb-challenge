import pytest
import datetime
from unbabel_cli.schema import MovingAverage
from unbabel_cli.data_processing.moving_average import aggregate_translation_delivered

def test_aggregate_translation_delivered():
    # Test with valid data
    valid_data = [
  {
    "timestamp": "2018-12-26 18:11:32.509654",
    "translation_id": "5aa5b2f39f7254a75a02",
    "source_language": "en",
    "target_language": "fr",
    "client_name": "taxi-eats",
    "event_name": "translation_started",
    "nr_words": 40,
    "duration": 52
  },
  {
    "timestamp": "2018-12-26 18:11:44.509654",
    "translation_id": "5aa5b2f39f7254a75a03",
    "source_language": "de",
    "target_language": "it",
    "client_name": "taxi-eats",
    "event_name": "translation_delivered",
    "nr_words": 74,
    "duration": 31
  },
    ]
    
    result = aggregate_translation_delivered(valid_data, 10)
    assert result == [MovingAverage(date=datetime.datetime(2018, 12, 26, 18, 11), average_delivery_time=31.0)]

    invalid_data = [
        {
            "timestamp": "2022-01-01T00:00:00Z",
            "translation_id": "123",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "client1",
            "event_name": "translation_started",
            "duration": 20,
            "nr_words": 100
        },
        {
            "timestamp": "2022-01-01T01:00:00Z",
            "translation_id": "124",
            "source_language": "en",
            "target_language": "de",
            "client_name": "client2",
            "event_name": "translation_started",
            "duration": 30,
            "nr_words": 200
        }
    ]
    result = aggregate_translation_delivered(invalid_data, 10)
    assert result == []