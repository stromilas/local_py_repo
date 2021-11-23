from dataclasses import dataclass


@dataclass
class Event:
    id: int
    type: str
    message: str
