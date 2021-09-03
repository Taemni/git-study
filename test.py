import requests

req = requests.get("https://iz-one.kr", headers={"User-Agent":"TEST"})

if req.status_code != 200:
    print("merge commit이 어떻게 ?d")
    print("mer")
    print(1)
    print(2)
    print(3)
    print(4)