# Dank memes
import discord
import random
import nextcord
from nextcord.ext import commands
import json
import urllib


UserInput = commands.Bot(command_prefix= "/")

async def ready():
    print("When Bot is ready")


@UserInput.command()
async def generateMeme(value):
    memeAPI = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")

    memeData = json.load(memeAPI)

    border = nextcord.Embed
