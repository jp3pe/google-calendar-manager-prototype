from runner import datetime_string_to_google_calendar_url_date_format_converter


def test_datetime_string_to_google_calendar_url_date_format_converter():
    assert datetime_string_to_google_calendar_url_date_format_converter("2023-07-21T10:00:00") == "20230721T100000"
