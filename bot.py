from asyncio import tasks
import random
import discord
import json
from discord.ext import commands

bot = commands.Bot()

@bot.event
async def on_ready():
    bot.change_presence(activity=discord.Game("seeking contributors!"))
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
            
with open('config.json') as f:
    config = json.load(f)
    
TOKEN = config['token']
bot.run(TOKEN)
    
