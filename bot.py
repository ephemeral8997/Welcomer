import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=None)

@bot.event
async def on_ready():
	print(bot.user.name)
	print(bot.user.id)
	await bot.change_presence(activity=discord.Activity(type=3, name='new members'))

@bot.listen()
async def on_message(member):
	guild = member.guild
	channel = guild.get_channel(638781504817987597)
	await channel.send(f'**Welcome {member.mention} to {guild.name}**')
	role = guild.get_role(622427088242343956)
	await member.add_roles(role)

@bot.listen()
async def on_message(member):
	guild = member.guild
	channel = guild.get_channel(638781530667352085)
	await channel.send(f'**{member.mention} left {guild.name}**')
	
bot.run('NjM5MTY3NDAzOTAwNTM0Nzky.XhGz4g.dX0_SJ_N948tnu7cZXtONyiRNuI')
