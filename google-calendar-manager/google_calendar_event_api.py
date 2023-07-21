import dataclasses
from datetime import datetime
from typing import List

DEFAULT_TIME_ZONE: str = "Asia/Seoul"


@dataclasses.dataclass
class GoogleCalendarEventApi:
    summary: str = "Event title"
    location: str = "Location"
    description: str = "Description about the event"
    start_date_time: str = datetime.today().isoformat(timespec="seconds")
    end_date_time: str = datetime.today().isoformat(timespec="seconds")
    start_time_zone: str = DEFAULT_TIME_ZONE
    end_time_zone: str = DEFAULT_TIME_ZONE
    attendees: List[str] = dataclasses.field(default_factory=list)
