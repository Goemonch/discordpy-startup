# coding: UTF-8
import os
import traceback
import random
import discord
from discord.ext import commands

from modules.grouping import MakeTeam


bot = commands.Bot(command_prefix='/')

"""起動処理"""
@bot.event
async def on_ready():
    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')


"""コマンド実行"""
# メンバー数が均等になるチーム分け
@bot.command()
async def mt(ctx, specified_num=2):
    make_team = MakeTeam()
    remainder_flag = 'true'
    msg = make_team.make_party_num(ctx,specified_num,remainder_flag)
    await ctx.channel.send(msg)

# メンバー数が均等にはならないチーム分け
@bot.command()
async def mmt(ctx, specified_num=2):
    make_team = MakeTeam()
    msg = make_team.make_party_num(ctx,specified_num)
    await ctx.channel.send(msg)

# メンバー数を指定してチーム分け
@bot.command()
async def grp(ctx, specified_num=1):
    make_team = MakeTeam()
    msg = make_team.make_specified_len(ctx,specified_num)
    await ctx.channel.send(msg)


"""日常会話"""
# メッセージ受信時に動作する処理
@bot.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 会話処理の中心部
    if message.content == 'おはよう':
        await message.channel.send('おはようにゃん！')
    if message.content == 'ポン':
        await message.channel.send('チーにゃん！')
    if message.content == 'ごんし':
        await message.channel.send('キモオタにゃん！')
    if message.content == 'くさぺこ':
        await message.channel.send('くさぺこにゃん！')
    if message.content == 'おやすみ':
        await message.channel.send('ちゃんと寝るにゃん！')
    if message.content == 'がっちゃん':
        await message.channel.send('ステロイダーにゃん！')
    if message.content == 'こんにちは':
        await message.channel.send('にゃーん！')
    if message.content == 'んにゃぴ':
        await message.channel.send('やじゅせんにゃーん！')
    if message.content == 'ごんずい':
        await message.channel.send('シイタケナメクジ野郎にゃん！')
    if message.content == 'ばるむ':
        await message.channel.send('スパイダーマにゃん！')
    if message.content == 'しこ':
        await message.channel.send('独りよがりにゃーん！')
    if message.content == 'ブラスク':
        await message.channel.send('自分の行ないが変化をもたらすかのように行動しなさい。\nそれが変化をもたらすのだ。')
    if message.content == 'めぐみん':
        await message.channel.send('すこ～')
    if message.content == 'なかの':
        await message.channel.send('azu is obunai')

    if message.content == 'map':
       bikkuri = ["輸送船がいいにゃん", "ダブルウイングがいいにゃん", "NIGHTTOWNがいいにゃん", "SABOTAGEがいいにゃん", "ツーフェイスがいいにゃん","RUSTがいいにゃん","ブルックリンがいいにゃん","ダストシールドがいいにゃん","コレクションがいいにゃん","城がいいにゃん","ペパカンがいいにゃん","古い神殿がいいにゃん","アウトポストがいいにゃん","ランガンがいいにゃん","チェックポイントがいいにゃん","ウルフスパイダーがいいにゃん"]
       choices = random.choice(bikkuri)
       await message.channel.send(choices)
    """メッセージ処理からコマンド処理に飛ばす"""
    await bot.process_commands(message)


"""botの接続と起動"""
bot.run("NzAyMzc3MDUxMDg4NDg2NDQx.Xp_Jpw.Hjgl2eJUieZzTY-ipNnamC1Tzi4")
