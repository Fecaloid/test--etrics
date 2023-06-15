from pydantic import BaseModel


class MetricRequestSerializer(BaseModel):
    service_name: str
    path: str
    response_time_ms: int


class MetricResponseSerializer(MetricRequestSerializer):
    id: str

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class MetricStatisticSerializer(BaseModel):
    path: str
    min_time: int
    max_time: int
    avg_time: float
    p99: float

    class Config:
        orm_mode = False
        allow_population_by_field_name = True


class MetricStatisticResponseSerializer(BaseModel):
    count: int
    items: list[MetricStatisticSerializer]
