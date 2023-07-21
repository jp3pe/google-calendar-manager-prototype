import dataclasses


@dataclasses.dataclass
class GoogleCalendarEventUrl:
    text: str
    date_from: str
    date_until: str
    stz: str
    etz: str
    details: str
    location: str
