url = "https://users.roblox.com/v1/users/{}"

req=requests.get(url.format(i))
local value = req.json()["displayName"]

def ReplaceLine(n,l,t):
    with open(n) as f:
        lines = file.readlins()
    lines[l] = t
    
ReplaceLine("main.lua",1,f"return {value}")
