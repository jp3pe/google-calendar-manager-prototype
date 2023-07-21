from urllib import parse

from google_calendar_event_url import GoogleCalendarEventUrl
from runner import datetime_string_to_google_calendar_url_date_format_converter


def test_url_generator():
    event_url = GoogleCalendarEventUrl(location=parse.quote("800 Howard St., San Francisco, CA 94103"),
                                       text=parse.quote("Google I/O 20123"),
                                       date_from=datetime_string_to_google_calendar_url_date_format_converter(
                                           "2023-07-28T09:00:00"),
                                       date_until=datetime_string_to_google_calendar_url_date_format_converter(
                                           "2023-07-28T17:00:00"),
                                       details=parse.quote("한국어 설명 테스트"),
                                       stz="Asia/Seoul",
                                       etz="Asia/Seoul"
                                       # stz="America/Los_Angeles",
                                       # etz="America/Los_Angeles",
                                       )
    url_goal = "https://calendar.google.com/calendar/r/eventedit?action=TEMPLATE&dates=20230728T090000" \
               "%2F20230728T170000&stz=Asia/Seoul&etz=Asia/Seoul&details=%ED%95%9C%EA%B5%AD%EC%96%B4%20%EC%84%A4%EB" \
               "%AA%85%20%ED%85%8C%EC%8A%A4%ED%8A%B8&location=800%20Howard%20St.%2C%20San%20Francisco%2C%20CA%2094103" \
               "&text=Google%20I/O%2020123"
    temp = event_url.url_generator()
    assert temp == url_goal
