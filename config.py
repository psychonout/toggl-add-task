def toggl_api():
    # to get at: https://developers.plan.toggl.com/applications
    return {
        "key": "",
        "secret": ""
    }


def toggl_creds():
    # your toggl account username and password
    return {
        "user": "",
        "pass": ""
    }


def endpoints():
    base = "https://api.plan.toggl.com/api/v5/"
    workspace = base + "274880/"
    return {
        "base": base,
        "auth_token": base + "authenticate/token",
        "workspace": workspace,
        "tasks": workspace + "tasks",
        "group": workspace + "groups/228450"
    }
