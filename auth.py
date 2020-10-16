import json
import os
import requests
import time
from base64 import b64encode
from config import toggl_api, toggl_creds, endpoints

SCRIPTS_FOLDER = os.path.realpath(__file__).replace("auth.py", "")
TOKEN_FILE = os.path.join(SCRIPTS_FOLDER, "toggl_token.json")


def modification_date(filename):
    return os.path.getmtime(filename)


def download_token():
    key = toggl_api()["key"]
    secret = toggl_api()["secret"]

    key_secret = f'{key}:{secret}'.encode('ascii')

    headers = {
        'Authorization': f'Basic {b64encode(key_secret).decode("utf-8")}'
    }

    auth_params = {
        "grant_type": "password",
        "username": toggl_creds()["user"],
        "password": toggl_creds()["pass"]
    }

    data = requests.post(endpoints()["auth_token"],
                         data=auth_params,
                         headers=headers).json()
    with open(TOKEN_FILE, "w") as f:
        json.dump(data, f)
    return data


def auth_header():
    try:
        with open(TOKEN_FILE, "r") as f:
            data = json.load(f)
        seconds_since = time.time() - modification_date(TOKEN_FILE)
        if seconds_since > data["expires_in"]:
            data = download_token()
    except Exception:
        data = download_token()
    result_header = {
        'Authorization': f'Bearer {data["access_token"]}'
    }
    return result_header
