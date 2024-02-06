import pytest
from unbabel_cli.data_validation.events_validator import events_input_validator, events_output_validator
from unbabel_cli.schema import MovingAverage

def test_events_input_validator():
    # Test with valid data
    valid_data = [
        {"timestamp": "2022-01-01T00:00:00Z", "translation_id": "123", "source_language": "en", "target_language": "fr", "client_name": "client1", "event_name": "translation_delivered", "duration": 20, "nr_words": 100},
        {"timestamp": "2022-01-01T01:00:00Z", "translation_id": "124", "source_language": "en", "target_language": "de", "client_name": "client2", "event_name": "translation_delivered", "duration": 30, "nr_words": 200}
    ]
    # Should not raise an exception
    events_input_validator(valid_data)


    # Test with invalid data
    invalid_data = [
        {"timestamp": "2022-01-01T00:00:00Z", "translation_id": "123", "source_language": "en", "target_language": "fr", "client_name": "client1", "event_name": "translation_delivered"},
        {"timestamp": "2022-01-01T01:00:00Z", "translation_id": "124", "source_language": "en", "target_language": "de", "client_name": "client2", "event_name": "translation_delivered", "duration": "30"}
    ]
    # Should raise a ValueError
    with pytest.raises(ValueError):
        events_input_validator(invalid_data)

def test_events_output_validator():
    # Test with valid data
    valid_data = [
        MovingAverage(date="2022-01-01T00:00:00Z", average_delivery_time=20),
        MovingAverage(date="2022-01-01T01:00:00Z", average_delivery_time=30)
    ]
    events_output_validator(valid_data)

    # Test with invalid data
    invalid_data = [
        {"date": "2022-01-01T00:00:00Z"},
        {"date": "2022-01-01T01:00:00Z", "average_delivery_time": "30"}
    ]

    with pytest.raises(TypeError):
        events_output_validator(invalid_data)