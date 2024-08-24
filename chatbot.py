import pip
import discord
import random
import requests 
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def display_waste(ctx):
    await ctx.send('$organic, $organic_waste, $plastic, $plastic_waste')

@bot.command()
async def plastic(ctx):
    await ctx.send('a synthetic material created from polymers derived from petroleum, while it is a versatile material its excessive use and lack of proper recycling have led to enviromental pollution')

@bot.command()
async def plastic_waste(ctx):
    await ctx.send('avoid using single use plastic that are non recycleable,  use reuseable paper bag for shopping and using a glass containers instead of plastic')

@bot.command()
async def organic(ctx):
    await ctx.send('any material that is biodegradable and comes from a plant or an animal')

@bot.command()
async def organic_waste(ctx):
    await ctx.send('composting waste, having a healthy diet and eat your meal before it starts moulding')

@bot.command()
async def mem(ctx):
    with open('images/curiga.png', 'rb') as f:
        # Mari simpan file perpustakaan/library Discord yang dikonversi dalam variabel ini!
        picture = discord.File(f)
   # Kita kemudian dapat mengirim file ini sebagai tolok ukur!
    await ctx.send(file=picture)

bot.run("MTI2NjY5OTU3NTQ0NDYzNTcxOQ.G_O-CR.fMOndJSC2LfAMVEZZn80qx8d1NtYH-l21p-ZmM")