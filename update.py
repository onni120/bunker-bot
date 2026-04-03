import os, re, requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

WEBHOOK = os.environ["DISCORD_WEBHOOK_URL"]
URL = "https://last-day-on-earth-survival.fandom.com/wiki/Bunker_Alfa"

r = requests.get(URL, headers={"User-Agent":"Mozilla"})
soup = BeautifulSoup(r.text, "html.parser")
text = soup.get_text(" ")

a = re.search(r"Android[^0-9]{0,80}(\d{5})", text)
i = re.search(r"iOS[^0-9]{0,80}(\d{5})", text)

def send(p, c):
    if not c: return
    requests.post(WEBHOOK, json={
        "content": f"BUNKER_ALFA|{p}|{c}|{datetime.now(timezone.utc).isoformat()}|fandom"
    })

send("android", a.group(1) if a else None)
send("ios", i.group(1) if i else None)
