#!/root/toggl_addtask/venv/bin/python
import sys
import random
import requests
from auth import auth_header
from config import endpoints
from datetime import datetime
from config import toggl_creds


def some_color():
    return "#%06x" % random.randint(0, 0xFFFFFF)


def add_task(name, timeframe, priority, date=datetime.now().date().isoformat()):
    color = str(some_color().lower())
    # high priority
    if (priority == 'hp'):
        project_id = 1496530
    # interuption 
    elif (priority == 'i'):
        project_id = 1496529
    # self development
    elif (priority == "sd"):
        project_id = 1496914
    else: 
        # maintanence
        project_id = 1496913
    params = {
        "color": color,
        "name": name,
        "start_date": date,
        "end_date": date,
        "estimated_minutes": timeframe,
        "status": "done",
        "user_id": toggl_creds()["id"],
        "project_id": project_id
    }
    result = requests.post(endpoints()["tasks"],
                  headers=auth_header(),
                  data=params)
    print(result)


if __name__ == "__main__":
    args = sys.argv[1:]
    name = args[0]
    timeframe = args[1]
    try:
        priority = args[2]
    except Exception:
        priority = "m"
    add_task(name, timeframe, priority)
