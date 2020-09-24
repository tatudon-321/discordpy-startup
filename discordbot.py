# -*- coding: utf-8 -*- #

import discord
from discord.ext import commands,tasks
import json
import random
import wikipedia
import wikidata.client
from PIL import Image, ImageDraw, ImageFont
import time
import asyncio
import datetime
import pickle
import sys
import platform
import re
from twitter import *
from dateutil.relativedelta import relativedelta as rdelta
import traceback
import os
import shutil
import pytz
import sqlite3
import aiohttp

#textto etc
import m10s_util as ut
from apple_util import AppleUtil
from l10n import TranslateHandler, LocalizedContext
#tokens
import config
#cog
from cogs import m10s_music
from cogs import m10s_info
from cogs import m10s_owner
from cogs import m10s_settings
from cogs import m10s_manage
from cogs import m10s_levels
from cogs import m10s_tests
from cogs import m10s_gcoms
from cogs import m10s_search
from cogs import m10s_other
from cogs import m10s_games
from cogs import P143_jyanken
from cogs import nekok500_mee6
from cogs import syouma
from cogs import pf9_symmetry
from cogs import apple_foc
from cogs import m10s_gban
from cogs import m10s_bmail
from cogs import m10s_auth_wiz

"""import logging
logging.basicConfig(level=logging.DEBUG)"""


bot = commands.Bot(command_prefix=('t!','t.'))
token = os.environ['DISCORD_BOT_TOKEN']
bot.owner_id = 541290054447005706

#エラーログ出すやつ
#@bot.event
#async def on_command_error(ctx, error):
    #orig_error = getattr(error, "original", error)
    #error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    #await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send(f'{ctx.bot.latency * 1000} ms')

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)
    
bot.remove_command("help")

@bot.command()
async def help(ctx):
    await ctx.send('未実装です。いずれ作ります')

@bot.command()
async def invite(ctx):
    await ctx.send('このbotの招待url|https://discord.com/api/oauth2/authorize?client_id=728281988892721254&permissions=0&scope=bot')

    
@bot.event
async def on_ready(): # botが起動したときに動作する処理
    print('bot is ready!!')
    await client.change_presence(activity=discord.Game(name="製作者|たつどん#2239", type=1))
    
bot.run(token)
