from __future__ import print_function


def main():
    url: str = "https://calendar.google.com/calendar/r/eventedit?action=TEMPLATE&dates=20230720T100000Z" \
               "%2F20230721T100000Z&stz=Asia/Seoul&etz=Asia/Seoul&details=This_is_event_created_by_link&location" \
               "=EVENT_LOCATION_HERE&text=Event_text"
    description_message: str = f'Please click the link to add an event into your Google Calendar: {url}'
    print(description_message)


if __name__ == '__main__':
    main()
