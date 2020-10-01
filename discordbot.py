import random
from discord.ext import commands
import asyncio
import traceback
import discord
import inspect
import textwrap
import importlib
from contextlib import redirect_stdout
import io
import os
import re
import sys
import copy
import time
import typing


bot = commands.Bot(command_prefix=('t!','t.'))
token = os.environ['DISCORD_BOT_TOKEN']
bot.owner_id = 541290054447005706

#エラーログ出すやつ
@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
@bot.command()
async def embed(ctx, *, text):
    embed.add_field(name=text, value=text)
    await ctx.send(embed=embed)

@bot.command()
async def ping(ctx):
    embed = discord.Embed(title='pingの測定結果',  color=0x000000)
    embed.add_field(name=f'{ctx.bot.latency * 1000} ms', value='PONG!')
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)
    
bot.remove_command("help")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='このbotのコマンドのhelpです', color=0x000000)
    embed.add_field(name='help　このコマンドを表示\nping  botのping速度を測ります\ninvite  botの招待リンク、公式サーバーのリンクを送信します\na',value='製作中です')
    await ctx.send(embed=embed)

@bot.command()
async def invite(ctx):
    embed = discord.Embed(title='このbotの招待リンク', description='下の青い文字をタップ or クリックすると招待できます。', color=0x000000)
    embed.add_field(name='[このBOTの招待](<https://discord.com/api/oauth2/authorize?client_id=728281988892721254&permissions=0&scope=bot>)', value='[公式サーバー](<https://discord.gg/pSZGXqZ>)')
    await ctx.send(embed=embed)
    
@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))
  
@bot.command()
async def htkz(ctx, amount: typing.Optional[int] = 1, *, liquid="beer"):
    await ctx.send('{}回{}をはたきます^ ^'.format(amount, liquid))
    
@bot.event
async def on_ready():
    activity = discord.Game(name="t!help|prefix|t! t.\n owner @たつどん#2239\n 公式サーバー→discord.gg/pSZGXqZ\n ver.2.0.1", type=3)
    await bot.change_presence(status=discord.Status.idle, activity=activity)
    print("Bot is ready!")

@bot.command()
async def dice(ctx):
    await ctx.send('…')
    
@bot.command()
async def update(ctx):
    embed = discord.Embed(title='このbotの最新のアップデート情報', description='ver.2.0.1', color=0x080000)
    embed.add_field(name='updateコマンドの修正をしました。', value='次回のアップデートに期待してください！\n アップデート日時|10/2 00:12')
    await ctx.send(embed=embed)
    #バージョンもくわえる！
 #botを止める用  
           

    
    
bot.run(token)
