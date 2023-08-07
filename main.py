from email import message
import os
import discord
from discord.ext import commands
import random  # 랜덤 함수 사용
import time  # 시간 관련 함수 사용
import sys
from keep_alive import keep_alive

import datetime  # 현재 시간 알기 위한 패키지
from discord.ext import tasks  # 반복 작업, 백그라운드 작업을 위한 패키지
from itertools import cycle

'''Web crawling'''
import requests
from bs4 import BeautifulSoup as bs  # 웹 크롤링을 위한 라이브러리
import re

TOKEN = os.environ['BOT_TOKEN_DDUGIBOT']  # 시스템 환경 변수에 접근해 토큰 값 불러옴
intents = discord.Intents.all()
prefix = '!'


bot = commands.Bot(
    command_prefix=prefix,  # 명령어 앞의 접두사 설정
    status=discord.Status.online,  # 상태 표시 설정
    activity=discord.Game("!명령어"),  # 상태 메시지 설정
    intents=intents  # 봇이 어떤 정보까지 접근할 것인지 설정
)


@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
    print(sys.version)

    keep_alive()
    print('keep_alive() started')


@bot.event
async def on_message(message):
    # 봇 자신이 보내는 메세지는 무시
    if message.author == bot.user:
        return

    # 명령어가 아닌 메시지들은 여기에서 처리
    if message.content == "안녕" or message.content == "하이":
        await message.channel.send("하이하이")

    if message.content == "해방":
        await message.channel.send("이화")

    if message.content == "열혈":
        await message.channel.send("공대")
    
    if message.content == "생동":
        await message.channel.send("전전")

    if message.content == "비상":
        await message.channel.send("이군...")

    if message.content == "영앤":
        await message.channel.send("프리")
    
    if message.content == "이서경" or message.content == "최지민":
        await message.channel.send("바보")
    
    if message.content == "어쩔":
        await message.channel.send("티비")

    # 명령어를 체크할 수 있도록 함
    await bot.process_commands(message)

@bot.command()
async def 명령어(message):
    명령어 = '아직 준비중이야~ 개발자한테 독촉 좀 해봐 '
    명령어 += 'ㅋ'
    await message.channel.send(명령어)

@bot.command()
async def hello(message):
    await message.channel.send('어르신, 기체후일향만강하시옵니까? 소자 뚜기봇 인사 여쭈옵니다.')

@bot.command()
async def 노래방점수(message):
    sing_score = random.randint(0, 100)
    msg = f'{message.author.name}님의 노래실력은...! {sing_score}점입니다! '
    if sing_score >= 90:
        msg += '참 잘했어요!'
    if sing_score < 10:
        msg += '...님 그거 사람이 부른 거 맞아요?'
    await message.channel.send(msg)

@bot.command()
async def 주사위(message):
    dice_num = random.randint(1, 6)  # 1 이상 6 이하 랜덤 정수
    await message.channel.send('떼구르르르 주사위가 굴러갑니다.')
    time.sleep(1)
    if dice_num == 1 or dice_num == 3 or dice_num == 6:
        dice_result = f'`{str(dice_num)}`이'
    else:
        dice_result = f'`{str(dice_num)}`가'
    await message.channel.send(f'멈춘 주사위에는 {dice_result} 적혀 있습니다.')

@bot.command()
async def 자판기(message):
    vending_effects = ['덜컹', '덜그럭', '덜커덩']
    vending_choices = ['자판기에 돈을 넣었지만 아무것도 나오지 않았습니다.',
                       '자판기에서 종이컵만 2개 뽑았습니다.',
                       '자판기에서 오렌지 쥬스를 뽑았습니다.',
                       '자판기에서 콜라를 뽑았습니다.',
                       '자판기에서 생수를 뽑았습니다.',
                       '자판기에서 핫초코를 뽑았습니다.',
                       '자판기에서 캔커피를 뽑았습니다.']
    special_effects_for_지아언니 = ['반짝거리는', 
                                    '영롱한 초록색의',
                                    '우주 최강의',
                                    '너무 맛있는']
    special_menu_for_지아언니 = ['민트초코 데자와를 뽑았습니다.',
                                 '민트초코우유를 뽑았습니다.',
                                 '민트초코 아이스크림을 뽑았습니다.',
                                 '민트초코 오레오를 뽑았습니다.',
                                 '민트초코 파르페를 뽑았습니다.',
                                 '민트초코라떼(hot)를 뽑았습니다.']

    if message.author.id == 1037981134505656330:
        await message.channel.send(f'({random.choice(special_effects_for_지아언니)}) {message.author.name}님이 {random.choice(special_menu_for_지아언니)}')
    else:
        await message.channel.send(f'({random.choice(vending_effects)}) {message.author.name}님이 {random.choice(vending_choices)}')


@bot.command()
async def 핑(message):
    await message.channel.send(f'퐁! {round(round(bot.latency, 4)*1000)}ms')  # 핑 체크


@bot.command()
async def 학식(message, 장소, 요일, 시간):
    장소목록 = ['진선미관', '헬렌관', '공대', '한우리집', '이하우스', '아이하우스']
    요일목록 = ['월', '화', '수', '목', '금', '토', '일']
    긴요일목록 = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    시간목록 = ['조식', '중식', '석식']

    if 요일 in 긴요일목록:
        요일 = 요일[0]  # '월요일' 형식으로 요일을 입력했으면 그중에 '월'만 떼어냄
    
    if not(요일 in 요일목록):
        msg = "요일을 바르게 입력해주세요!"
        await message.channel.send(msg)
        return


    if 장소 == 장소목록[0]:  # 진선미관
        articleNo = 903
    elif 장소 == 장소목록[1]:  # 헬렌관
        if 시간 == '조식' or 시간 == '석식':
            msg = "학식이 없는 시간입니다. 다른 시간을 선택해주세요!"
            await message.channel.send(msg)
            return
        articleNo = 902
    elif 장소 == 장소목록[2]:  # 공대
        if 시간 == '조식' or 시간 == '석식':
            msg = "학식이 없는 시간입니다. 다른 시간을 선택해주세요!"
            await message.channel.send(msg)
            return
        articleNo = 905
    elif 장소 == 장소목록[3]:  # 한우리집
        articleNo = 899
    elif 장소 == 장소목록[4]:  # 이하우스
        articleNo = 900
    elif 장소 == 장소목록[5]:  # 아이하우스
        articleNo = 339841
    else:
        msg = "등록되지 않은 장소입니다!\n등록된 장소 : "
        for i in 장소목록:
            msg += i + ", " 
        await message.channel.send(msg[:-2])
        return
   
    url = "https://www.ewha.ac.kr/ewha/life/restaurant.do?mode=view&articleNo=" + str(articleNo) + "&article.offset=0&articleLimit=10"
    page = requests.get(url)

    soup = bs(page.text, "html.parser")  # 응답받은 HTML 내용을 Beautifulsoup 클래스의 객체로 생성
    day = soup.select('.b-menu-day > .b-day')  # 요일 긁어오기

    if 시간 == 시간목록[0]:    # 조식
        
        lunch = soup.select('.b-menu-day > .b-menu-b > div > pre')  # 조식 메뉴만 긁어오기
    elif 시간 == 시간목록[1]:  # 중식
        lunch = soup.select('.b-menu-day > .b-menu-l > div > pre')  # 중식 메뉴만 긁어오기
    elif 시간 == 시간목록[2]:  # 석식
        lunch = soup.select('.b-menu-day > .b-menu-d > div > pre')  # 중식 메뉴만 긁어오기
    else:
        msg = "시간을 정확하게 입력해주세요!\n[조식/중식/석식]"
        await message.channel.send(msg)
        return

    for i, day in enumerate(day, 1):
        if 요일 == 요일목록[i-1]:
            try:
                lunchmenu = str(lunch[i-1]).replace("<pre>", "")
                lunchmenu = lunchmenu.replace("</pre>", "")
                lunchmenu = lunchmenu.replace("*", "\*")
                lunchmenu = lunchmenu.replace("&lt;", "\<")
                lunchmenu = lunchmenu.replace("&gt;", "\>")
            except:
                continue
            msg = "============================\n" + 장소 + " " + re.sub(r"\s", "", day.text) + " " + 시간 + " 메뉴\n============================\n" + lunchmenu + "\n============================"
            break
    
    await message.channel.send(msg)


@학식.error
async def 학식_에러(message, error):
    msg = prefix + "학식 [장소] [요일] [조식/중식/석식]"
    await message.channel.send(msg)


bot.run(TOKEN)