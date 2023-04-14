import discord
import random   
# print(discord.__version__)
# client 是我們與 Discord 連結的橋樑，intents 是我們要求的權限
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
tmpList = []
#調用event函式庫
@client.event
#當機器人完成啟動時
async def on_ready():
    print('目前登入身份：',client.user)

@client.event
#當有訊息時
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    print("test")
    if message.author == client.user:
        return
    #如果以「說」開頭
    if message.content.startswith('?eat'):

      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) >2:
        await message.channel.send("要連在一起啦")
      if len(tmp) == 2:
        if tmp[1]=="show":
            await message.channel.send(",".join(tmpList))
        else:
        # await message.channel.send("test")
            print("add",tmp[1])
            tmpList.append(tmp[1])
            await message.channel.send("已新增"+str(tmp[1]))
      else:#隨機
        test = random.randint(0, len(tmpList)-1)
        print("ran",test)
        await message.channel.send(tmpList[test])
      

client.run("MTA5NjI4MzU4ODUxMDYyNTgxNA.GUuOmq.RnlP7qtzRVlC9sfQGcjvf7vndce1OMigwi0AWE") #TOKEN 在剛剛 Discord Developer 那邊「BOT」頁面裡面