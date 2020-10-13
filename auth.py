import json
import os
import requests
import time
from base64 import b64encode
from config import toggl_api, toggl_creds

TOKEN_FILE = "toggl_token.json"


def modification_date(filename):
    return os.path.getmtime(filename)


def download_token():
    base = "https://api.plan.toggl.com/api/v5/"
    workspace = "274880/"
    auth_endpoint = f"{base}{workspace}authenticate/token"

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

    data = requests.post(auth_endpoint,
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
        else:
            seconds_until = data["expires_in"] - seconds_since
            print(f"Seconds till token expires: {seconds_until}")
    except Exception:
        data = download_token()
    result_header = {
        'Authorization': f'Bearer {data["access_token"]}'
    }
    return result_header
