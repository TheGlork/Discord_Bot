import discord
from discord.ext import commands
import os
import certifi

os.environ['SSL_CERT_FILE'] = certifi.where()

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command(name='ping')
async def ping(ctx):
    await ctx.send('Pong!')

@bot.tree.command(name="hello", description="Say hello!")
async def hello(interaction: discord.Interaction):
    await interaction.response.send_message(f'Hello, {interaction.user.mention}!')

@bot.event
async def on_ready():
    await bot.tree.sync()  
    print(f'Logged in as {bot.user}!')

bot.run('API_KEY')
