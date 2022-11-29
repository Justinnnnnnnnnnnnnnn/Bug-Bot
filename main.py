import os
import discord
import random
from discord.ext import commands
from requests import get
import json

TOKEN = 'MTAzOTY3MTMyNjc5NDg0NjMwOA.GY8ybo.dSFdoRJelBYB6lAveGTVYTmisFfsuqzDJAwct8'

client = discord.Client(intents=discord.Intents.all())


bot = commands.Bot(intents=discord.Intents.all(), command_prefix = '/')


client_1 = commands.Bot(intents = discord.Intents.all(), command_prefix = '/meme')

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

# @client_1.command()
# async def test(ctx):
#    await ctx.reply("Testing")


# @client_1.command()
# async def Memes(ctx):
#     content = get("https://meme-api.herokuapp.com/gimme%22").text 

#     data = json.loads(content,)

#     memeData = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")

#     await ctx.reply(embed=memeData)


@client.event
async def on_message(message):

    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')


    if message.content.startswith('/meme'):
        content = get("https://meme-api.herokuapp.com/gimme%22").text 

        data = json.loads(content,)

        memeData = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")

        await message.channel.send(embed=memeData)


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
            role = 'Butterfly'
        elif count <= 10:
            role = 'Ant'

        await message.channel.send(f"Congrats!! You've been selected for the {role} role")
        give_role = discord.utils.get(message.guild.roles, name= role)
        await message.author.edit(roles=[give_role])

    if message.content.startswith('/madlib'):
        channel = message.channel
        await channel.send('Welcome to mab libs! You will be asked to give a number of nouns, adjectives, verbs, and more. At the end, everything you pick will be put together into a customized story. Press (x) to continue. Enter quit at any time to stop.')
        storeInp = []

        def check(m):
            return m.content == 'x'

        m = await client.wait_for('message', check=check)
        # got user input showing to start.
        await message.channel.send('Enter an adjective.')

        def check(m):
            return m.content != 'quit'
        
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter an adjective.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a number.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a noun.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            

        await message.channel.send('Enter a honorific.')  # ???
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a name.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb ending in -ing.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)

        await message.channel.send('Enter a singular noun.')  # or change to body part
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a verb.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send('Enter a number.')
        m = await client.wait_for('message', check=check)
        if m.content != 'quit':
            storeInp.append(m.content)
            
        await message.channel.send(f'Just another {storeInp[0]} day as i {storeInp[1]} at my computer. Yet again my {storeInp[2]} refused to work. It should be {storeInp[3]}, but no, my {storeInp[4]} never wants to {storeInp[5]}. Even after {storeInp[6]} hours, I still keep getting {storeInp[7]} errors. My teacher, {storeInp[8]} {storeInp[9]} said I just need to {storeInp[10]} but my code still keeps {storeInp[11]}. I am about to {storeInp[12]} my {storeInp[13]} {storeInp[14]} if it doesn\'t work after {storeInp[15]} more tries.')

client.run(TOKEN)