from pydantic import BaseModel, Field, StrictFloat, field_validator
from datetime import datetime

class Event(BaseModel):
    timestamp: datetime = Field(..., description="The timestamp of the event")
    translation_id: str = Field(..., description="The ID of the translation")
    source_language: str = Field(..., description="The source language of the translation")
    target_language: str = Field(..., description="The target language of the translation")
    client_name: str = Field(..., description="The name of the client")
    event_name: str = Field(..., description="The name of the event")
    duration: int = Field(..., description="The duration of the event")
    nr_words: int = Field(..., description="The number of words in the translation")

    @field_validator('timestamp')
    def validate_timestamp(cls, v):
        if not isinstance(v, datetime):
            raise ValueError('timestamp must be a datetime')
        return v

    @field_validator('duration', 'nr_words')
    def validate_positive(cls, v):
        if v < 0:
            raise ValueError('duration and nr_words must be positive')
        return v


class MovingAverage(BaseModel):
    date: datetime = Field(..., description="The date of the moving average calculation")
    average_delivery_time: StrictFloat = Field(..., description="The average delivery time")

    @field_validator('average_delivery_time')
    def round_average_delivery_time(cls, v):
        rounded_value = round(v, 1)
        if rounded_value.is_integer():
            return int(rounded_value)
        return rounded_value