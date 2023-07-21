from __future__ import print_function

import dataclasses
import datetime
from typing import List
from urllib import parse

DEFAULT_TIME_ZONE: str = "Asia/Seoul"


# TODO: Separate dataclasses into other files
@dataclasses.dataclass
class GoogleCalendarEventApi:
    summary: str = "Event title"
    location: str = "Location"
    description: str = "Description about the event"
    start_date_time: str = datetime.datetime.today().isoformat(timespec="seconds")
    end_date_time: str = datetime.datetime.today().isoformat(timespec="seconds")
    start_time_zone: str = DEFAULT_TIME_ZONE
    end_time_zone: str = DEFAULT_TIME_ZONE
    attendees: List[str] = dataclasses.field(default_factory=list)


@dataclasses.dataclass
class GoogleCalendarEventUrl:
    text: str
    date_from: str
    date_until: str
    stz: str
    etz: str
    details: str
    location: str


def datetime_string_to_google_calendar_url_date_format_converter(datetime_string: str) -> str:
    datetime_string_split = datetime_string.split('T')
    date = datetime_string_split[0].split('-')
    time = datetime_string_split[1].split(':')

    year, month, day = map(lambda e: e, date)
    hour, minute, second = map(lambda e: e, time)

    return f"{year}{month}{day}T{hour}{minute}{second}"


def main():
    new_event: GoogleCalendarEventApi = GoogleCalendarEventApi()
    # Get user input about Google Calendar event
    print("Let's create a link for new event in Google Calendar!")
    new_event.summary = parse.quote(input("Name of the event: "))
    new_event.location = parse.quote(input("Location of the event: "))
    new_event.description = parse.quote(input("Description of the event: "))
    date_from = input("Date from(ex: 2023-01-01T10:00:00): ")
    date_until = input("Date until(ex: 2023-01.02T11:00:00): ")
    new_event.start_date_time = datetime_string_to_google_calendar_url_date_format_converter(date_from)
    new_event.end_date_time = datetime_string_to_google_calendar_url_date_format_converter(date_until)

    url: str = f"https://calendar.google.com/calendar/r/eventedit?action=TEMPLATE&dates={new_event.start_date_time}" \
               f"%2F{new_event.end_date_time}&stz={new_event.start_time_zone}&etz={new_event.end_time_zone}&details" \
               f"={new_event.description}&location" \
               f"={new_event.location}&text={new_event.summary}"
    description_message: str = f'Please click the link to add an event into your Google Calendar: {url}'
    print(description_message)


if __name__ == '__main__':
    main()
