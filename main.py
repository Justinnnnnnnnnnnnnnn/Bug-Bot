import os
import discord
import random
from discord.ext import commands
from requests import get
import json

TOKEN = 'MTAzOTY3MTMyNjc5NDg0NjMwOA.GY8ybo.dSFdoRJelBYB6lAveGTVYTmisFfsuqzDJAwct8'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

bot = commands.Bot(intents=discord.Intents.all(), command_prefix = '/')


client = commands.Bot(intents = discord.Intents.all(), command_prefix = '/meme')


@client.command()
async def test(ctx):
   await ctx.reply("Testing")


@client.command()
async def Memes(ctx):
    content = get("https://meme-api.herokuapp.com/gimme%22").text 

    data = json.loads(content,)

    memeData = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")

    await ctx.reply(embed=memeData)


@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

  
    if message.author == client.user:
        return
    if message.content.startswith('/quiz'):
        channel = message.channel
        await channel.send('Welcome to the role determiner quiz! press (x) to continue')

        def check(m):
            return m.content == 'x' 

        await client.wait_for('message', check=check)
        await message.channel.send("Question 1/5: It's a dark stormy night... What do you do?: \n (a) Hide under the cover where it's safe\n (b) Go out and explore... who knows what you might find\n (c) Relax and appreciate it, you've always enjoyed storms\n (d) Call up your friends its the perfect night for get together")

        global count
        global role
        global give_role
        
        def check(m):
            global count 
            count = 0
            if m.content == 'a':
                count = count + 1
                print(count)
            elif m.content == 'b':
                count = count + 5
                print(count)
            elif m.content == 'c':
                count = count + 3
                print(count)
            elif m.content == 'd':
                count = count + 7
                print(count)
            return count, m.content == 'a' or 'b' or 'c' or 'd' and count
        
        await client.wait_for('message', check=check)
        await message.channel.send("Question 2/5: What word would the people closest to you best use to describe you?: \n (a) Daring \n (b) Reserved \n (c) Caring \n (d) Optimistic")
        
        def check(m):
            global count 
            if m.content == 'a':
                count = count + 7
                print(count)
            elif m.content == 'b':
                count = count + 1
                print(count)
            elif m.content == 'c':
                count = count + 3
                print(count)
            elif m.content == 'd':
                count = count + 5
                print(count)
            return count, m.content == 'a' or 'b' or 'c' or 'd' and count
        
        await client.wait_for('message', check=check)
        await message.channel.send("Question 3/5: What smell comes to mind when you think of home?: \n (a) Fresh cookies right out of the oven \n (b) Brewing coffee \n (c) Early morning spring rain \n (d) Simple vanilla " )

        def check(m):
            global count
            if m.content == 'a':
                count = count + 7
                print(count)
            elif m.content == 'b':
                count = count + 3
                print(count)
            elif m.content == 'c':
                count = count + 5
                print(count)
            elif m.content == 'd':
                count = count + 1
                print(count)
            return count, m.content == 'a' or 'b' or 'c' or 'd' and count
        
        await client.wait_for('message', check=check)
        await message.channel.send("Question 4/5: What color could you never get sick of?: \n (a) Vibrant yellow \n (b) Pastel blue \n (c) Apple red \n (d) Forestly green")

        def check(m):
            global count
            if m.content == 'a':
                count = count + 5
                print(count)
            elif m.content == 'b':
                count = count + 3
                print(count)
            elif m.content == 'c':
                count = count + 7
                print(count)
            elif m.content == 'd':
                count = count + 1
                print(count)
            return count, m.content == 'a' or 'b' or 'c' or 'd' and count
        
        await client.wait_for('message', check=check)
        await message.channel.send("Question 5/5: If you could go back in time which era?: \n (a) To the dinosaur age \n (b) The 90's! \n (c) The future instead! \n (d) The Roaring 20's")
  
        def check(m):
            global count
            if m.content == 'a':
                count = count + 1
                print(count)
            elif m.content == 'b':
                count = count + 5
                print(count)
            elif m.content == 'c':
                count = count + 3
                print(count)
            elif m.content == 'd':
                count = count + 7
                print(count)
            return m.content == 'a' or 'b' or 'c' or 'd' and count
        
        await client.wait_for('message', check=check)
        if count > 25:
            role = 'Spider'
        elif count > 20:
            role = 'Ladybug'
        elif count > 15:
            role = 'Dragonfly'
        elif count > 10:
            role = 'Buttlerfly'
        elif count <= 10:
            role = 'Ant'

        await message.channel.send(f"Congrats!! You've been selected for the {role} role")
        give_role = discord.utils.get(message.guild.roles, name= role)
        await message.author.edit(roles=[give_role])

client.run(TOKEN)