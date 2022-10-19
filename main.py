from webserver import keep_alive
import requests

channelID = 1025465996200386581
headers = {
    "authorization":
    "MTAzMTkwNDQwODU2NjUwNTQ5Mg.GjU8HG.XF5yd1XryulxWIUlnuB0V84xw-kkoad4TVbjKg"
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
