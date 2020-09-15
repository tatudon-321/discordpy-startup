import discord, os
from discord.ext import tasks
from discord.ext import commands 
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv(verbose=True)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

bot = commands.Bot(command_prefix=('t.','!t','t!','tatu'))
