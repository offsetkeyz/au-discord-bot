import random
import discord
import json
from discord.ext import commands, tasks
from discord import Embed

bot = commands.Bot()

@bot.event
async def on_ready():
    status_task.start()
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
    
@bot.slash_command(name = "contribute", description = "Run this command for more information on how to contribute to the bot.")
async def contribute(ctx):
    await ctx.respond("""
                      In order to contribute to the bot, head over to github.com/offsetkeyz/au-discord-bot and follow the instructions there.\n
                      If you need ideas for contributions, run the command /todos
                      """)

@bot.slash_command(name = "todo", description = "Get ideas for contributions") 
async def todos(ctx):
    embed = Embed(title="Ideas for Contributions")
    with open('bot.py') as f:
        code = f.read()
    todos = []
    for line in code.split('\n'):
        if "#TODO " in line:
            todos.append(line.strip())
    if todos:
        i = 1
        for todo in todos:
            embed.add_field(name=f"Idea {i}", value=todo, inline=False)
            i=i+1
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("No TODOs, but don't let that stop you!")

@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Setup the game status task of the bot
    """
    statuses = ["seeking contributors!", "please contribute!"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))
            
with open('config.json') as f:
    config = json.load(f)
    
TOKEN = config['token']
bot.run(TOKEN)
   
   
   
#TODO Create an RSS reader for different feeds in CS
