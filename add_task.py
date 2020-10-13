#!/root/toggl_addtask/venv/bin/python
import sys
import random
import requests
from auth import auth_header
from config import endpoints
from datetime import datetime


def some_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def add_task(name, timeframe, date=datetime.now().date().isoformat()):
    color = str(some_color().lower())
    params = {
        "color": color,
        "name": name,
        "start_date": date,
        "end_date": date,
        "estimated_minutes": timeframe,
        "status": "done",
        "user_id": 6567265
    }
    requests.post(endpoints()["tasks"],
                  headers=auth_header(),
                  data=params)


if __name__ == "__main__":
    args = sys.argv[1:]
    name = args[0]
    timeframe = args[1]
    add_task(name, timeframe)
