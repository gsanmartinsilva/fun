import discord
from discord.ext import commands
import os
import time
import random
import asyncio

# import movies
with open('movies.txt') as f:
    movies = f.readlines()
# Create bot
bot = commands.Bot(command_prefix="$")

palabritas = ["primera", "segunda", "tercera",
              "cuarta", "quinta", "sexta",
              "septima", "octava", "novena",
              "decima", "oncedécima", "docema"]

@bot.command()
async def agua(ctx, n):
    
    # prepare randomness
    random.shuffle(movies)
    # start communication
    await ctx.channel.send(f'Ya, al agua se van {n} películas 🎥')
    await asyncio.sleep(3)
    for i in range(int(n)):
        await ctx.channel.send(f"La {palabritas[i]} al aguaaaaa 🤽‍♀️🥁🥁🥁🥁🥁🥁")
        await asyncio.sleep(2)
        await ctx.channel.send(f'{movies[i].upper()} 😢')
        await asyncio.sleep(4)
    # la que salio
    await ctx.channel.send('AHORA! La próxima películita que veremos eeeeeeeeeees!')
    await asyncio.sleep(4)
    await ctx.channel.send(f"{movies[int(n)+1].upper()} 😃")
     
        
 


bot.run(os.getenv('TOKEN'))