import requests



r = requests.get("https://www.google.com/search?q=la+anh+mp3")
with open("html.html", "w", encoding="utf-8") as f:
    f.write(r.text)
