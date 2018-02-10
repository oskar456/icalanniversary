
import os
import glob
import uuid

import yaml
from icalendar import Calendar, Event, vText, vRecur, vFrequency
from datetime import datetime, timedelta
from slugify import slugify


def load_data(datadir):
    for f in glob.glob(os.path.join(datadir, "*.yaml")):
        with open(f) as inf:
            for d in yaml.safe_load_all(inf):
                d['filename'] = os.path.basename(f)[:-5]
                yield d


def icalevent(e):
    if not all(prop in e for prop in ['date', 'title']):
        return
    iev = Event()
    iev.add('dtstamp', datetime.now())
    iev.add('dtstart', e['date'])
    iev.add('dtend', e['date'] + timedelta(1))
    rrule = vRecur()
    rrule['freq'] = vFrequency('yearly')
    iev.add('rrule', rrule)
    iev.add('summary', vText("{:04d}: {}".format(e['date'].year,
                                                 e['title'])))
    iev.add('uid', "{}@icalaniversary.invalid".format(
        slugify(iev['summary'])))
    desc = [e.get('link'), e.get('desc')]
    if any(desc):
        desc = "\n".join([x for x in desc if x])
        iev.add('description', vText(desc))
    return iev


def main():
    datadir = './data'
    outdir = './out'
    events = list(load_data(datadir))
    print(events)
    outfname = os.path.join(outdir, 'all.ics')
    cal = Calendar()
    cal.add('version', '2.0')
    cal.add('prodid', '-//icalanniversary////')

    for e in events:
        event = icalevent(e)
        print(event.to_ical())







