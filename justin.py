# Dank memes
import discord
from discord.ext import commands
from requests import get
import json

client = commands.Bot(intents = discord.Intents.all(), command_prefix = '/meme')


@client.command()
async def test(ctx):
   await ctx.reply('Testing')

   
@client.command()
async def Memes(ctx):
    content = get('https://meme-api.herokuapp.com/gimme').text # API

    data = json.loads(content,)

    memeData = discord.Embed(title=f"{data['title']}", Color = discord.Color.random()).set_image(url=f"{data['url']}")

    await ctx.reply(embed=memeData)


client.run('MTAzOTY3MTMyNjc5NDg0NjMwOA.GY8ybo.dSFdoRJelBYB6lAveGTVYTmisFfsuqzDJAwct8') # Needs the token