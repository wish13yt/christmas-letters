from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import discord
from discord import app_commands

intents = discord.Intents.default()
intents.message_content = True

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()
        print("Slash commands synced")

client = MyClient(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$ping'):
        await message.channel.send('Pong! Ho ho ho! Merry Christmas! 🎄🎄🎄')

@client.tree.command()
async def info(interaction: discord.Interaction):
    """Information about licenses used by this bot and the bot itself."""
    with open("info.txt", "r") as file:
        infofr = file.read()
    await interaction.response.send_message(infofr)

@client.tree.command()
@app_commands.describe(
    text='What do you want to write today?',
    font='What font do you want? (Options: Rubik Gemstones or Open Sans) Default: Open Sans'
)
async def letter(interaction: discord.Interaction, text:str, font:str):
    """Write a beautiful letter! (Note: Gets sent to whole chat)"""
    peakfonts = ["Rubik Gemstones", "Open Sans"]
    try:
        img = Image.open("letter.png")
        draw = ImageDraw.Draw(img)
        if font == "Rubik Gemstones":
            thefont = "Rubik_Gemstones/RubikGemstones-Regular.ttf"
        if font == "Open Sans" or font not in peakfonts:
            thefont = "Open_Sans/static/OpenSans-Regular.ttf"
        font = ImageFont.truetype(thefont, 32)
        draw.text((100, 100), text, (255,255,255), font=font)
        img.save('generated/letter.png')
        await interaction.response.send_message(file=discord.File("generated/letter.png"))
    except:
        await interaction.response.send_message("There was a very jolly issue!! Ho ho ho!")


client.run('add your token here')