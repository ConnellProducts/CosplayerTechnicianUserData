url = "https://users.roblox.com/v1/users/{}"
isRandom = None
i = 34

if isRandom != None:
    i =random.randrange(1, 60000001)
req=requests.get(url.format(i))
print(req.json()["displayName"])
