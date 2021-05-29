from discord.ext import commands
from discord.ext import tasks
import os
import traceback
import discord

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']
CHANNEL_ID = os.environ['DISCORD_POST_CHANNEL']
client = discord.Client()


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    

# 60秒に一回ループ
@tasks.loop(seconds=60)
async def loop():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('時間だよ')  

#ループ処理実行
loop.start()

bot.run(token)
