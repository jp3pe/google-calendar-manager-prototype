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

    def url_generator(self) -> str:
        return f"https://calendar.google.com/calendar/r/eventedit?action=TEMPLATE&dates={self.date_from}" \
               f"%2F{self.date_until}&stz={self.stz}&etz={self.etz}&details" \
               f"={self.details}&location={self.location}&text={self.text}"
