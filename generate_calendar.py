from datetime import datetime, timedelta
from icalendar import Calendar, Event
import pytz
from pathlib import Path

tz = pytz.timezone("US/Alaska")  # Change if needed

cal = Calendar()
cal.add('prodid', '-//VRBO Auto Blocker//mxm.dk//')
cal.add('version', '2.0')

start = datetime.now(tz) + timedelta(days=10)
end = datetime.now(tz) + timedelta(days=365)

cur = start
while cur <= end:
    ev = Event()
    ev.add('summary', 'Blocked')
    ev.add('dtstart', cur.date())
    ev.add('dtend', (cur + timedelta(days=1)).date())
    ev.add('transp', 'OPAQUE')
    cal.add_component(ev)
    cur += timedelta(days=1)

Path("docs").mkdir(exist_ok=True)
with open("docs/vrbo_blocker.ics", "wb") as f:
    f.write(cal.to_ical())
