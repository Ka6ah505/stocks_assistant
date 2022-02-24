from pydantic import BaseModel


class Record(BaseModel):
    ticket: str
    date_candle: int
    open: float
    high: float
    low: float
    close: float
    volume: int
    time_frame: str
    id: int

    class Config:
        orm_mode = True


class RecSt(BaseModel):
    id: int
    ticket: str
    close: float = None

    class Config:
        orm_mode = True
