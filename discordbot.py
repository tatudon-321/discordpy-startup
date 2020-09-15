import discord
import datetime
import asyncio
import random
import json
import urllib.request
import urllib.parse
import re
import os
import traceback

from discord.ext import commands

bot = commands.Bot(command_prefix="k!",help_command=commands.HelpCommand(command_attrs={'hidden': True}))
client = discord.Client()

token = os.environ['DISCORD_BOT_TOKEN']
members = {
    "たつどん": 'https://media.discordapp.net/attachments/741658483711279175/755460447834210424/image0.jpg',}


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)
