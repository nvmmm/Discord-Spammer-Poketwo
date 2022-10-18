from webserver import keep_alive
import requests

channelID = 1025465996200386581
headers = {
    "authorization":
    ""MTAzMTUxOTM2NTYzMzQxMzE3MA.GG8m2j.e5_fo_9DyC0rQED3g6oLosHG4lJPFv2XflWD1E""
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})
