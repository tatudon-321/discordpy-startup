from discord.ext import commands
import os
import traceback


bot = commands.Bot(command_prefix=('t.','t!','T.','T!'))
token = os.environ['DISCORD_BOT_TOKEN']

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

    
@client.event
async def on_ready(): # botが起動したときに動作する処理
    print('bot is ready!!')
    await client.change_presence(activity=discord.Game(name="製作者|たつどん#2239", type=1))
    
bot.run(token)
