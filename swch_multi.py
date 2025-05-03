import requests
from datetime import datetime
import pytz

TASK_ID = TASK ID HERE
TOKEN = "YOUR SWCH TOKEN HERE"
STUDENT_ID = 
ST_ANS_AID = FIRST ANSWER AID HERE
ANSC = ANSWER COUNT

ANSWERS = []

for i in range(ANSC):
    ANSWERS.append({"aid": ST_ANS_AID + i})

url = f"https://api.szkolawchmurze.org/students/{STUDENT_ID}/update_checked_task/"

headers = {
    "accept": "application/json, text/plain, */*",
    "accept-language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
    "authorization": TOKEN,
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
    "worksheet_student_check": STUDENT_ID,
    "task_data": {
        "task_id": TASK_ID,
        "task_type": "MULTI_OPTION",
        "answers": ANSWERS,
    },
    "task": TASK_ID,
}

response = requests.patch(url, headers=headers, json=data)

fin = ""
for i in range(ANSC):
    fin += response.json()['task_data']['answers'][i]['points'].__str__()

print(url)
print(f"Status code: {response.status_code}")
print(fin)

# 1 means to check this answer
