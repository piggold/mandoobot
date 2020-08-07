from chdp import CHDPClient
from discord import Embed, Color
import os
import random
import asyncio
from random import choice


client = CHDPClient(prefix = '만두봇 ')
token = os.environ['TOKEN']



@client.event
async def on_ready():
    print(client.user.name)
    print('활성화 되었습니다')
    await client.change_presence_loop(games = [f'저는 {len(client.guilds)}개의 서버에 들어가있어요!       ', '이 메세지는 5초마다 바뀌어요       ', '" 만두봇 도움말" 을 쳐주세요        ', '이 봇은 유튜버 찐만두가 만들었어요!       '])

@client.event
async def on_message(message):
    await client.use_cmd(message)
    prefix = '만두봇 '
    if message.author.bot: return
    if str(message.channel.type) != 'text': return
    if not message.content.startswith(prefix): return

    cmd = message.content.split(prefix)[1].split(' ')[0]
    args = message.content.split(cmd)[1][1:].split(' ')


client.run(token)