from telethon.sync import TelegramClient, events
from config import api_hash, api_id
import time
import requests
import sys


# https://www.youtube.com/watch?v=bON-KPiiNCk

# https://source.unsplash.com/1600x900/?nature,water

with TelegramClient('anon', api_id, api_hash) as client:

    @client.on(events.NewMessage(pattern=r"^hi"))
    async def hi(event):
        await event.reply("hi how can i help  you")

    @client.on(events.NewMessage(pattern=r"^\.info"))
    async def reg(event):
        me = await client.get_me()
        await event.reply(me.stringify())

    @client.on(events.NewMessage(pattern=r"\.conversations"))
    async def infoconv(event):
        async for dailog in client.iter_dialogs():
            print(dailog.name + " has id " + str(dailog.id))
        # await event.reply("p")

    @client.on(events.NewMessage(pattern=r"\.text ."))
    async def texting(event):
        text = event.message.raw_text
        await event.reply(text)

    @client.on(events.NewMessage(pattern=r"\.send"))
    async def sending(event):
        await client.send_message("sajawalhacker", "hi me is sended")
        # await event.reply(text)

    @client.on(events.NewMessage(pattern=r"\.hack"))
    async def hack(event):
        await event.edit("trying to get the weakness...")
        time.sleep(1)
        await event.edit("[...                         ] 5%")
        time.sleep(1)
        await event.edit("[.....                       ] 10%")
        time.sleep(1)
        await event.edit("[.......                     ] 15%")
        time.sleep(1)
        await event.edit("[.........                   ] 20%")
        time.sleep(1)
        await event.edit("[..........                  ] 35%")
        time.sleep(1)
        await event.edit("[...........                 ] 45%")
        time.sleep(1)
        await event.edit("[.............               ] 50%")
        time.sleep(1)
        await event.edit("[...............             ] 60%")
        time.sleep(1)
        await event.edit("[.................           ] 70%")
        time.sleep(1)
        await event.edit("[....................        ] 75%")
        time.sleep(1)
        await event.edit("[........................    ] 80%")
        time.sleep(1)
        await event.edit("[..........................  ] 90%")
        time.sleep(1)
        await event.edit("[............................] 100%")
        time.sleep(1)
        await event.edit("gained access...")
        time.sleep(1)
        await event.edit("You are HAcked Buddy...")
        time.sleep(1)
        await event.edit("Just Joking Buddy...")
        time.sleep(1)

    @client.on(events.NewMessage(pattern=r"\.gdn"))
    async def gdn(event):
        await event.edit("😴🥱😴🥱")
        time.sleep(1)
        await event.edit("🥱😴🥱😴")
        time.sleep(1)
        await event.edit("😴🥱😴🥱")
        time.sleep(1)
        await event.edit("🥱😴🥱😴")
        time.sleep(1)
        await event.edit("😴🥱😴🥱")
        time.sleep(1)
        await event.edit("🥱😴🥱😴")
        time.sleep(1)
        await event.edit("""
              ｡♥️｡･ﾟ♡ﾟ･｡♥️｡･｡･｡･｡♥️｡･
╱╱╱╱╱╱╱╭╮╱╱╱╭╮╱╭╮╭╮
╭━┳━┳━┳╯┃╭━┳╋╋━┫╰┫╰╮
┃╋┃╋┃╋┃╋┃┃┃┃┃┃╋┃┃┃╭┫
┣╮┣━┻━┻━╯╰┻━┻╋╮┣┻┻━╯
╰━╯╱╱╱╱╱╱╱╱╱╱╰━╯
   ｡♥️｡･ﾟ♡ﾟ･｡♥️° ♥️｡･ﾟ♡ﾟ
      """)

    @client.on(events.NewMessage(pattern=r"\.pic .",outgoing=True))
    async def sendpic(event):
        command = event.raw_text.split(" ")
        keyword = command[1]
        url = f"https://source.unsplash.com/1600x900/?{keyword},{keyword}"
        r = requests.get(url)

        with open("temp.jpg","wb") as file:
            file.write(r.content)
        print("downloaded")

        to_id = event.to_id

        await client.send_file(to_id,"temp.jpg")

    client.run_until_disconnected()
