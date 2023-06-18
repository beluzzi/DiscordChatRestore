import time
import datetime

from discordwebhook import Discord
import json

directory = 'chats'
discord = Discord(
    url="https://discord.com/api/webhooks/1119982778214256804/zgIbMI3-7L0yTKf115LKbntXew74saDSUpuM_XVia_JQfHjlUyhRaCTeP5dOowjjmbtq")


def restore(file):
    f = open(file, encoding='utf-8')
    data = json.load(f)
    counter = 0
    wait = 1
    for i in data['messages']:
        time.sleep(1.5)
        if bool(i["mentions"]):
            msg = str(i["content"])
            x = (len(i["mentions"]))
            for y in range(x):
                nname = i["mentions"][y]["nickname"]
                uid = i["mentions"][y]["id"]
                msg = msg.replace("@" + nname, "<@" + uid + ">")
            discord.post(
                content=msg,
                username=i["author"]["nickname"],
                avatar_url=i["author"]["avatarUrl"],
            )
        if bool(i["attachments"]):
            x = (len(i["attachments"]))
            for y in range(x):
                discord.post(
                    content=i["attachments"][y]["url"],
                    username=i["author"]["nickname"],
                    avatar_url=i["author"]["avatarUrl"]
            )
        else:
            discord.post(
                content=i["content"],
                username=i["author"]["nickname"],
                avatar_url=i["author"]["avatarUrl"],
            )
        counter += 1
        wait += 1
        if (wait % 100) == 0:
            time.sleep(5)
        print(str(round(counter / len(data['messages']), 5) * 100) + " % done sending (" + str(
            counter) + ") messages sent " + "time left ~: " + str(datetime.timedelta(
            seconds=(len(data['messages']) - counter) * 1.5 + ((len(data['messages']) - counter) // 100) * 5)))


if __name__ == '__main__':
    restore("chats/💎 El Sharqi 💎 - Voice Channels - general [1024362942302539867].json")
