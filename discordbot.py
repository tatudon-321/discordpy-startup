from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    embed = discord.Embed(title='pingの測定結果', description='PONG!', color=0x000000)
    embed.add_field(name='結果', value=f'{ctx.bot.latency * 1000} ms')
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)

@bot.event
async def on_ready():
    activity = discord.Game(name="t!help\n prefix→t! !t t. tatu\n owner @たつどん#2239\n 公式サーバー→作成中", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    
bot.run(token)
