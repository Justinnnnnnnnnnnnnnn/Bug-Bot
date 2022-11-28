# Dank memes
import discord
import random
import nextcord
from nextcord.ext import commands
import json
import urllib


UserInput = commands.Bot(command_prefix= "/meme")

async def ready():
    print("When Bot is ready")


@UserInput.command()
async def generateMeme(run):
    memeAPI = urllib.request.urlopen("https://meme-api.herokuapp.com/gimme")

    memeData = json.load(memeAPI)

    memeURL = memeData["title"]

    memeName = memeData["url"]


    border = nextcord.Embed(title = memeName, color = nextcord.colour.gray())

    border.set_image(url = memeURL)

    await run.send(border = border)

