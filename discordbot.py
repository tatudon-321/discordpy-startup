from discord.ext import commands
import os
import traceback
import typing
import discord


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
async def ping(ctx):
    embed = discord.Embed(title='pingの測定結果', description='PONG!', color=0x000000)
    embed.add_field(value=f'{ctx.bot.latency * 1000} ms')
    await ctx.send(embed=embed)

@bot.command()
async def say(ctx, *, text):
    await ctx.send(text)
    
bot.remove_command("help")

@bot.command()
async def help(ctx):
    embed = discord.Embed(title='このbotのコマンドのhelpです', color=0x00000)

@bot.command()
async def invite(ctx):
    await ctx.send('このbotの招待url|https://discord.com/api/oauth2/authorize?client_id=728281988892721254&permissions=0&scope=bot')
    
@bot.command()
async def bottles(ctx, amount: typing.Optional[int] = 99, *, liquid="beer"):
    await ctx.send('{} bottles of {} on the wall!'.format(amount, liquid))
    
async def is_owner(ctx):
    return ctx.author.id == 316026178463072268

@bot.command(name='eval')
@commands.check(is_owner)
async def _eval(ctx, *, code):
    """A bad example of an eval command"""
    await ctx.send(eval(code))
    
bot.run(token)
