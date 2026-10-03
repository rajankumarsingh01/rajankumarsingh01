"""Refreshes the 'Recently shipped' block in README.md with your latest pushed repos."""
import json, os, sys, urllib.request
from datetime import datetime, timezone

USER = "rajankumarsingh01"
README = sys.argv[1] if len(sys.argv) > 1 else "README.md"
HIDE = {"mern_practice_self"}   # repos you do not want shown (add names here)
START, END = "<!--RECENT_ACTIVITY:START-->", "<!--RECENT_ACTIVITY:END-->"

def ago(iso):
    d = datetime.now(timezone.utc) - datetime.fromisoformat(iso.replace("Z", "+00:00"))
    if d.days >= 30: return f"{d.days // 30} mo ago"
    if d.days >= 1: return f"{d.days}d ago"
    if d.seconds >= 3600: return f"{d.seconds // 3600}h ago"
    return "just now"

req = urllib.request.Request(
    f"https://api.github.com/users/{USER}/repos?sort=pushed&per_page=30&type=owner",
    headers={"Accept": "application/vnd.github+json", "User-Agent": "readme-updater",
             **({"Authorization": f"Bearer {os.environ['GITHUB_TOKEN']}"} if os.environ.get("GITHUB_TOKEN") else {})})
repos = json.load(urllib.request.urlopen(req))
repos = [r for r in repos if not r["fork"] and r["name"].lower() != USER.lower() and r["name"] not in HIDE][:5]

lines = []
for r in repos:
    desc = f" — {r['description']}" if r.get("description") else ""
    lines.append(f"- [**{r['name']}**]({r['html_url']}){desc} · _pushed {ago(r['pushed_at'])}_")
block = "\n".join(lines) if lines else "- Nothing pushed recently."

text = open(README, encoding="utf-8").read()
if START not in text or END not in text:
    sys.exit("Markers not found in README")
head, rest = text.split(START, 1)
_, tail = rest.split(END, 1)
open(README, "w", encoding="utf-8").write(f"{head}{START}\n{block}\n{END}{tail}")
print(block)
