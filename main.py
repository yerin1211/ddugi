from email import message
import os
import discord
from discord.ext import commands
import random  # 랜덤 함수 사용
import time  # 시간 관련 함수 사용

TOKEN = os.environ.get('BOT_TOKEN_DDUGIBOT')  # 시스템 환경 변수에 접근해 토큰 값 불러옴
intents = discord.Intents.all()

bot = commands.Bot(
    command_prefix='!',  # 명령어 앞의 접두사 설정
    status=discord.Status.online,  # 상태 표시 설정
    activity=discord.Game("!명령어"),  # 상태 메시지 설정
    intents=intents  # 봇이 어떤 정보까지 접근할 것인지 설정
)
 
@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')

@bot.command()
async def 명령어(message):
    명령어 = '내가 기능이 뭐가 있겠니? hello밖에 못함 수고~'
    명령어 += 'ㅋ'
    await message.channel.send(명령어)

@bot.command()
async def hello(message):
    await message.channel.send('어르신, 기체후일향만강하시옵니까? 소자 뚜기봇 인사 여쭈옵니다.')
 
@bot.command()
async def 핑(message):
    await message.channel.send(f'퐁! {round(round(bot.latency, 4)*1000)}ms')  # 핑 체크




















bot.run('MTAzNTc2MjMyOTU0OTI5NTY3Nw.GALZOL.AxKScS2I8duKXQLf8QIUjlrDPKxovStdI6QMKI')