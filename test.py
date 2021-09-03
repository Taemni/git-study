import requests

req = requests.get("https://iz-one.kr", headers={"User-Agent":"TEST"})

if req.status_code == 200:
    print("성공!")