import requests

req = requests.get("https://iz-one.kr", headers={"User-Agent":"DEV"})

if req.status_code != 200:
    print("실패!")