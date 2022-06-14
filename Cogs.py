from fileinput import filename
import graph
import steam
import g2a
import numpy as np
from matplotlib import pyplot as plt
import discord 
from discord.ext import commands
import math
from io import BytesIO

class Price(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command()
  async def pricomp(self, ctx, *, game):
    async with ctx.typing():
        steam_id, steam_price, steam_discount = steam.scrape(game)
        g2a_price, g2a_discount = g2a.get_prices(game)
        embed = discord.Embed(title=f"Price of {game} on different platforms", color=0xFF5733)
        embed.set_image(url = f"https://cdn.akamai.steamstatic.com/steam/apps/{steam_id}/header.jpg")
        embed.add_field(name="Steam", value=f"Price: {steam_price}\nDiscount: {steam_discount}%", inline = True)
        embed.add_field(name="G2A", value=f"Price: {g2a_price}\nDiscount: {g2a_discount}%", inline = True)
        await ctx.send(embed=embed)

class Help(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command(pass_context = True)
  async def h(self, ctx):
    async with ctx.typing():

      embed = discord.Embed(
        title="List of Commands",
        color = 0xFF5733
      )

      embed.set_author(name='Help')
      embed.add_field(name='$pricomp "game"', value='Will return prices on Steam and G2A')
      embed.add_field(name='$graphing', value='Will return a graph of your function. You need to write it a such for it to work "x**3+2"')
      embed.add_field(name='$zeros', value='Will return the zeroes of a functions (Not in the imaginary one yet). You need to give the a, b and c parameters as such: $zeros 3 4 5')
      embed.add_field(name='$h', value='Will return this message')
      await ctx.send(embed=embed)



class Graph(commands.Cog):
  def __init__(self, bot):
     self.bot = bot
  @commands.command()
  async def graphing(self, ctx, function):
    async with ctx.typing():
      plt.clf() 

      x = np.linspace(-5, 5, 100)

      f = eval(function)

      plt.plot(x, f, color="red")
      plt.grid()

      plt.savefig(fname = "plot.png")

      file = discord.File("plot.png", filename="plot.png")
      
      embed = discord.Embed(title=f"{ctx.message.author} Graph", color=0xFF5733)
      embed.set_image(url = "attachment://plot.png")
      await ctx.send(function)
      await ctx.send(file=file, embed=embed)

class Zeros(commands.Cog):
  def __init__(self, bot):
    self.bot = bot
  @commands.command()
  async def zeros(self, ctx, *args):
      a = int(args[0])
      b = int(args[1])
      c = int(args[2])

      delta = (b*b) - 4*a*c

      if delta > 0:
        async with ctx.typing():
          x_1 = (-b + math.sqrt(delta))/2*a
          x_2 = (-b - math.sqrt(delta))/2*a
          await ctx.send(f"x1 is equal to: {x_1} and x_2 is equal to: {x_2}")
      elif delta == 0:
        async with ctx.typing():
          x = (-b)/2*a
          await ctx.send(f"The only solution is {x}")
      else:
        async with ctx.typing():
          await ctx.send("There is no solution... Except in the imaginary realm ;)")

      