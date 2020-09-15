    embed = discord.Embed(title='最新のアップデート情報',description='現在のtatudonbotのバージョン:2.0.0', color=0x505080)
    embed.add_field(name='・試験的にbotを永続起動させることに成功しました。それに伴ってinviteコマンドを復活させました。',value='次回のアップデートに期待してください！\n アップデート日時 2020 8/26 PM15:26')
    await ctx.send(embed=embed)
    
@bot.command()
async def say2(ctx, *args):
    await ctx.send('{} 単語数: {}'.format(len(args), ', '.join(args)))

@bot.command()
async def helptest(ctx):
    embed = discord.Embed(title='コマンドジャンル一覧', description='見たいジャンルの数字を発言してください', color=0x400040)
    embed.add_field(name='i', value='a')
    await ctx.send(embed=embed)
    
#プレイ中表示

@bot.event
async def on_ready():
    activity = discord.Game(name="t!help\n prefix→t! !t t. tatu\n owner @たつどん#2239\n 公式サーバー→作成中", type=3)
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print("Bot is ready!")
    
@bot.command()
async def taiyaki(ctx):
    await ctx.send('<@342179214038007810>さん！愛してます！')
 
@bot.event
async def on_ready():
    # 起動時にメッセージの送信
    channel = client.get_channel(754617937968758845)
    await channel.send('監視してるよ＾＾')
    
# メッセージを受けた時の動作
@bot.event
async def on_message(message):
    # イベント入るたびに初期化はまずいのでグローバル変数で
    global ModeFlag
    # botの発言は無視する(無限ループ回避)
    if message.author.bot:
        return
    # 一応終了するコマンドも用意しておく
    if message.content == '!exit':
        await message.channel.send('ﾉｼ')
        sys.exit()
    # google検索モード(次に何か入力されるとそれを検索)
    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        # 日本語で検索した上位5件を順番に表示
        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
               break
    # google検索モードへの切り替え
    if message.content == '!google':
        ModeFlag = 1
        await message.channel.send('検索するワードをチャットで発言してね')
    # 単純な応答
    if message.content == 'bot君いる？':
        await message.channel.send('私bot君。あなたの後ろにいるよ。')
    # 特定の文字から始まる文章が発言されたとき
    if message.content.startswith('負け'):
        lose = message.author.name + "の負け！ｗ"
        await message.channel.send(lose)
    #リプライを受け取った時
    if client.user in message.mentions:
        reply = f'{message.author.mention} うるさいよ。'
        await message.channel.send(reply)
    # これについては触れないよ。
    if message.content.startswith("なんだかんだ"):
        kanda = "かんだ・・・神田ァ！？\n" + "https://www.youtube.com/watch?v=KUwpssJX37M"
        await message.channel.send(kanda)

bot.run(os.environ.get("token"))
