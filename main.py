import requests
from secret import API_TOKEN
from datetime import date, datetime, timedelta, timezone
import argparse
import json

parser = argparse.ArgumentParser(description="Toggl Anonymizer")
parser.add_argument(
    "-d",
    "--date",
    nargs="?",
    type=lambda d: datetime.strptime(d, "%Y-%m-%d").date(),
    help="Date to transfer, YYYY-MM-DD",
    default=date.today(),
)
date = parser.parse_args().date

f = open("./settings.json")
settings = json.load(f)
f.close()

api_url = "https://api.track.toggl.com/api/v9"

with requests.Session() as session:
    # login
    session.post(f"{api_url}/me/sessions", auth=(API_TOKEN, "api_token"))

    entries = session.get(
        f"{api_url}/me/time_entries",
        params={"start_date": date, "end_date": date + timedelta(days=1)},
    )
    for entry in entries.json():
        if (
            entry["workspace_id"] == settings["from"]["workspace_id"]
            and entry["project_id"] == settings["from"]["project_id"]
        ):
            start = datetime.combine(
                date, datetime.strptime(settings["to"]["time"], "%H:%M").time()
            ).astimezone(timezone.utc)
            response = session.post(
                f"{api_url}/workspaces/{settings['to']['workspace_id']}/time_entries",
                headers={"content-type": "application/json"},
                json={
                    "created_with": "Toggl Anonymizer",
                    "description": entry["description"],
                    "duration": entry["duration"],
                    "project_id": settings["to"]["project_id"],
                    "start": start.strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "workspace_id": settings["to"]["workspace_id"],
                },
            )
