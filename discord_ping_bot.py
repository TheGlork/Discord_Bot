import discord
from discord.ext import commands
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

# Create an instance of the bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a simple prefix command
@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

# Define a simple slash command
@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}!')

# Sync the slash commands when the bot is ready
@bot.event
async def on_ready():
    await bot.tree.sync()  # This syncs the slash commands with Discord
    print(f'Logged in as {bot.user}!')

# Run the bot with your token
bot.run('MTI4MDM5MDY1MTQzOTIxODcxMA.GnnsWr.lKGOUKLefDyjA9--egxr3Y9wpbBJ7PNYkauGGo')
