import random
import discord
import json
from discord.ext import commands, tasks
from discord import Embed
from discord.commands import Option
import openai

bot = commands.Bot()

@bot.event
async def on_ready():
    status_task.start()
    print(f"{bot.user} is ready and online!")
    
@bot.slash_command(name = "hello", description = "Say hello to the bot")
async def hello(ctx):
    await ctx.respond("Hey!")
    
@bot.slash_command(name = "ask_aubie", description="Ask Aubie Anything!")
async def ask_aubie(ctx: discord.ApplicationContext, message: Option(str)):
    await ctx.respond(f"You asked: '{message}'")
    response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message,
            max_tokens=100,
            n=1,
            stop=None,
            temperature=0.5
        )
    embed = Embed(title=f"{message}", description=response)

    try:
        await ctx.respond(embed=embed)
    except Exception as f:
        print(f'F {f}')
    
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

openai.api_key = config['openai']
openai.organization = config['organization']

bot.run(TOKEN)
   
   
   
#TODO Create an RSS reader for different feeds in CS
#TODO Command that shows advisors and their contact information.
#TODO Scrape data from Auburn's Website and feed it to a channel
#TODO Ask ChatGPT Bot
