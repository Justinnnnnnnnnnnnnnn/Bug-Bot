import os
import discord
import random
from discord.ext import commands
import pandas as pd
from datetime import datetime

TOKEN = 'MTAzOTY3MTMyNjc5NDg0NjMwOA.GY8ybo.dSFdoRJelBYB6lAveGTVYTmisFfsuqzDJAwct8'

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

bot = commands.Bot(intents=discord.Intents.all(), command_prefix = '/')

def export_csv():
    """
    Converts table from html code to a list of its values then converts to csv
    file.
    csv file header: ,Date,Visitor,G,Home,G.1,Unnamed: 5,Att.,LOG,Notes
    csv file line 1: 
    0,2022-10-07,San Jose Sharks,1.0,Nashville Predators,4.0,,16648.0,2:43,"at (Prague, CZ)"
    """
    df = pd.read_html("https://www.hockey-reference.com/leagues/NHL_2023_games.html")
    df[0].to_csv('scores.csv')

def load_scores(file):
    """
    Takes a file as a parameter, reads csv file line for line and stores
    the date as a key and value a list of information of the game:
    first team name, first team score, second team name, second team score
    If there are no updated scores and the fields are empty for the scores 
    it stops storing information.
    Returns scores as a dictionary.
    ex. '2022-10-11': ['Vegas Golden Knights', '4', 
                       'Los Angeles Kings', '3', 
                       'Tampa Bay Lightning', '1', 
                       'New York Rangers', '3']
    """
    scores = {}
    f = open(file)
    f.readline()
    for line in f:
        info = line.strip().split(',')
        if info[3] == '':
            break
        line_num, date = info[0], info[1]
        team1, score1, team2, score2 = info[2], info[3], info[4], info[5]
        score1 = str(int(float(score1)))
        score2 = str(int(float(score2)))
        if date not in scores:
            scores[date] = [team1, score1, team2, score2]
        else:
            scores[date] += [team1, score1, team2, score2]
    f.close()
    return scores

def get_current_date():
    """
    Gets current date with datetime.now(), formats it and returns it as a 
    string.
    ex. '2022-10-11'
    """
    now = str(datetime.now())
    formatted_date = ''
    for c in now:
        if c == ' ':
            break
        else:
            formatted_date += c
    return formatted_date

def get_recent_scores(scores):
    """
    dictionary : '2022-10-11': ['Vegas Golden Knights', '4', 
                                'Los Angeles Kings', '3', 
                                'Tampa Bay Lightning', '1', 
                                'New York Rangers', '3']
    """
    recent_scores = []
    

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

    if message.content.startswith('/nhlscores'):
        export_csv()
        scores = load_scores('scores.csv')
        current_date = get_current_date()
        await message.channel.send("Let me update you on the most updated hockey scores as best as I can!")
        await message.channel.send()
    
    if message.content.startswith('/test'):
        await message.channel.send("This is a test I see it needs a string for a parameter\nam I on a new line now?")
        await message.channel.send("Can I do two seperate messages?")
client.run(TOKEN)