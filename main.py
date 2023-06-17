import time
import datetime

from discordwebhook import Discord
import json

directory = 'chats'
discord = Discord(
    url="https://discord.com/api/webhooks/1119642697590898729/URF0uiDm5VZc_dEt_S_1A8rUt2A8MS2OH33JoISR2opSVuhNkqZIW8GLqRYlX7mE_FGq")


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
        else:
            discord.post(
                content=i["content"],
                username=i["author"]["nickname"],
                avatar_url=i["author"]["avatarUrl"],
            )
        if bool(i["attachments"]):
            discord.post(
                content=i["attachments"][0]["url"],
                username=i["author"]["nickname"],
                avatar_url=i["author"]["avatarUrl"]
            )
        counter += 1
        wait += 1
        if (wait % 100) == 0:
            time.sleep(60)
        print(str(round(counter / len(data['messages']), 5) * 100) + " % done sending (" + str(
            counter) + ") messages sent " + "time left ~: " + str(datetime.timedelta(
            seconds=(len(data['messages']) - counter) * 1.5 + ((len(data['messages']) - counter) // 100) * 60)))


if __name__ == '__main__':
    restore("test.json")
