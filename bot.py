import random
import discord
import json
from discord.ext import commands, tasks
from discord import Embed
import os

bot = commands.Bot()

aubie_chat_bot = App()
aubie_chat_bot.add("web_page", "https://bulletin.auburn.edu/undergraduate/samuelginncollegeofengineering/departmentofcomputerscienceandsoftwareengineering/bachelorofcomputerscience_major/")

@bot.event
async def on_ready():
    status_task.start()
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
    
@bot.slash_command(name = "contribute", description = "Run this command for more information on how to contribute to the bot.")
async def contribute(ctx):
    embed = Embed(title="How you can contribute", description="This will provide you with all the info you need to contribute to the bot")
    embed.add_field(name="How?", value="Head over to github and read the README. This will explain everything you need to know.", inline=False)
    embed.add_field(name="Ideas", value = "If you are looking for ideas to contribute, run the command /todo")
    embed.url = "https://github.com/offsetkeyz/au-discord-bot"
    await ctx.respond(embed=embed)
    
@bot.slash_command(name = "todo", description = "Get ideas for contributions") 
async def todo(ctx):
    embed = Embed(title="Ideas for Contributions")
    with open('bot.py') as f:
        code = f.read()
    todos = []
    for line in code.split('\n'):
        if "#TODO " in line and not line.strip().startswith('if'):
            todos.append(line.strip())
    if todos:
        i = 1
        for todo in todos:
            todo_stripped = todo.replace("#TODO","",1)
            embed.add_field(name=f"Idea {i}", value=todo_stripped, inline=False)
            i=i+1
        await ctx.respond(embed=embed)
    else:
        await ctx.respond("No TODOs, but don't let that stop you!")
        
@bot.slash_command(name = "ask_aubie", description = "Ask Aubie anything about the program!") 
async def todo(ctx, message: discord.Message):
    embed = Embed(title="Ideas for Contributions")
    embed.add_field(name=message, value=aubie_chat_bot.query(message))
    await ctx.respond(embed=embed)

@tasks.loop(minutes=1.0)
async def status_task() -> None:
    """
    Setup the game status task of the bot
    """
    statuses = ["seeking contributors!", "please contribute!"]
    await bot.change_presence(activity=discord.Game(random.choice(statuses)))
            
with open('config.json') as f:
    config = json.load(f)
    
os.environ["OPENAI_API_KEY"] = config['openai']
from embedchain import App
TOKEN = config['token']
bot.run(TOKEN)
   
   
   
#TODO Create an RSS reader for different feeds in CS
#TODO Command that shows advisors and their contact information.
#TODO Scrape data from Auburn's Website and feed it to a channel
#TODO Ask ChatGPT Bot
