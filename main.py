import discord
from discord.ext import commands
from Cogs import Price, Help, Graph, Zeros

f = open("token.txt")

token = f.readline()

bot = commands.Bot(command_prefix='$')

bot.add_cog(Price(bot))
bot.add_cog(Help(bot))
bot.add_cog(Graph(bot))
bot.add_cog(Zeros(bot))

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

bot.run(token)