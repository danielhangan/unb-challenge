import datetime
from unbabel_cli.schema import MovingAverage
from unbabel_cli.data_processing.moving_average import calculate_moving_average

def test_aggregate_translation_delivered():
    # Test with valid data
    valid_data = [
        {
            "timestamp": "2018-12-26 18:11:08.509654",
            "translation_id": "5aa5b2f39f7254a75aa5",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "airliberty",
            "event_name": "translation_delivered",
            "nr_words": 30,
            "duration": 20
        },
        {
            "timestamp": "2018-12-26 18:15:19.903159",
            "translation_id": "5aa5b2f39f7254a75aa4",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "airliberty",
            "event_name": "translation_delivered",
            "nr_words": 30,
            "duration": 31
        },
        {
            "timestamp": "2018-12-26 18:23:19.903159",
            "translation_id": "5aa5b2f39f7254a75bb3",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "taxi-eats",
            "event_name": "translation_delivered",
            "nr_words": 100,
            "duration": 54
        }
        ]
    
    result = calculate_moving_average(valid_data, 10)
    expected_result = [
        MovingAverage(date="2018-12-26 18:11:00", average_delivery_time=0),
        MovingAverage(date="2018-12-26 18:12:00", average_delivery_time=20),
        MovingAverage(date="2018-12-26 18:13:00", average_delivery_time=20),
        MovingAverage(date="2018-12-26 18:14:00", average_delivery_time=20),
        MovingAverage(date="2018-12-26 18:15:00", average_delivery_time=20),
        MovingAverage(date="2018-12-26 18:16:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:17:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:18:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:19:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:20:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:21:00", average_delivery_time=25.5),
        MovingAverage(date="2018-12-26 18:22:00", average_delivery_time=31),
        MovingAverage(date="2018-12-26 18:23:00", average_delivery_time=31),
        MovingAverage(date="2018-12-26 18:24:00", average_delivery_time=42.5)
    ]
    
    assert result == expected_result

    invalid_data = [
        {
            "timestamp": "2022-01-01 00:00:00.509654",
            "translation_id": "123",
            "source_language": "en",
            "target_language": "fr",
            "client_name": "client1",
            "event_name": "translation_started",
            "duration": 20,
            "nr_words": 100
        },
        {
            "timestamp": "2022-01-01 01:00:00.509654",
            "translation_id": "124",
            "source_language": "en",
            "target_language": "de",
            "client_name": "client2",
            "event_name": "translation_started",
            "duration": 30,
            "nr_words": 200
        }
    ]
    result = calculate_moving_average(invalid_data, 10)
    assert result == []