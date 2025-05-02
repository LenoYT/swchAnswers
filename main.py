import requests
from datetime import datetime
import pytz

url = "https://api.szkolawchmurze.org/students/URID/update_checked_task/"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": "UR_TOKEN",
    "content-type": "application/json",
    "origin": "https://platforma.szkolawchmurze.org",
    "priority": "u=1, i",
    "referer": "https://platforma.szkolawchmurze.org/",
    "sec-ch-ua": '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "x-swchr-localdatetime": datetime.now(pytz.timezone("Europe/Warsaw")).isoformat()
}

data = {
    "worksheet_student_check": TASKID,
    "task_data": {
        "task_id": 23912,
        "task_type": "MULTI_OPTION",
        "answers": [
            {"aid": 673513},
            # {"aid": 673514},
            # {"aid": 673515},
            # {"aid": 673516},

            # {"aid": 673517},
            # {"aid": 673518},
            # {"aid": 673519},
            # {"aid": 673520}
        ]
    },
    "task": TASKID
}

response = requests.patch(url, headers=headers, json=data)

print(f"Status code: {response.status_code}")
try:
    print("Response:", response.json()["answers"])
except Exception:
    print("Response (non-JSON):", response.text)
