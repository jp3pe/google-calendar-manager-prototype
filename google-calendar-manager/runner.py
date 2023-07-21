from urllib import parse

from google_calendar_event_api import GoogleCalendarEventApi
from google_calendar_event_url import GoogleCalendarEventUrl


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
    new_event.summary = input("Name of the event: ")
    new_event.location = input("Location of the event: ")
    new_event.description = input("Description of the event: ")
    # TODO: Add function to input timezone(ex: America/Los_Angeles, Asia/Seoul)
    new_event.start_date_time = input("Date from(ex: 2023-01-01T10:00:00): ")
    new_event.end_date_time = input("Date until(ex: 2023-01.02T11:00:00): ")

    new_event_url = GoogleCalendarEventUrl(text=parse.quote(new_event.summary),
                                           date_from=datetime_string_to_google_calendar_url_date_format_converter(
                                               new_event.start_date_time),
                                           date_until=datetime_string_to_google_calendar_url_date_format_converter(
                                               new_event.end_date_time),
                                           stz=new_event.start_time_zone,
                                           etz=new_event.end_time_zone,
                                           details=parse.quote(new_event.description),
                                           location=parse.quote(new_event.location)
                                           )

    url: str = new_event_url.url_generator()
    print(f'Please click the link to add an event into your Google Calendar: {url}')


if __name__ == '__main__':
    main()
