from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord
from datetime import datetime

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_POST_CHANNEL']
client = discord.Client()
channel_sent = None

@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

"""
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
"""

@tasks.loop(seconds=60)
async def timeloop():
    now = datetime.now().strftime('%H:%M')
    if now == '22:54':
        await channel_sent.send(f"今日の予定\n{member_mention} テスト")#f文字列
        
@client.event
async def on_ready():
    global channel_sent
    global member_mention
    member_mention = "<@609895586979643415>"
    channel_sent = client.get_channel(848287069217620038)
    timeloop.start() #定期実行するメソッドの後ろに.start()をつける

bot.run(token)
