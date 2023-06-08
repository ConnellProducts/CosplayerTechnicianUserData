-- read remote file from website
http = require("socket.http")
local body, code = socket.http.request("https://users.roblox.com/v1/users/3687992703")
if not body then error(code) end

return print(body)

--[[ read local file 
local open = io.open
local file = open("file.json", "rb")
if not file then return nil end
local jsonString = file:read "*a"
file:close()

-- parse json with lunajson
local json = require 'lunajson'
local t = lunajson.decode(jsonString)
print(t)]]
