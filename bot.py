import discord
from discord import ActivityType as a
from discord.ext import commands

bot = commands.Bot(command_prefix=None)
footer = "Programmer welcomer / Support server"
emo = '<:welcomer:667276923021295626>'

@bot.event
async def on_ready():
	print(bot.user.name)
	print(bot.user.id)
	activity = discord.Activity(type=a.watching)
	activity.name = "new members!"
	await bot.change_presence(activity=activity, status=discord.Status.idle)

@bot.listen()
async def on_command(ctx):
	pass

@bot.listen()
async def on_member_join(member):
	guild = member.guild
	channel = guild.get_channel(638781504817987597)
	if member.bot:
		role = guild.get_role(668393208438456332)
		await member.add_roles(role)
		em = discord.Embed(colour=0xffff00)
		em.set_author(name="Member joined!")
		em.description = f'A bot called {member.name} joined to us!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text=footer, icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	else:
		role = guild.get_role(668392530542329856)
		await member.add_roles(role)
		em = discord.Embed(colour=0xffff00)
		em.set_author(name="Member joined!")
		em.description = f'A programmer called {member.name} joined to us!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text=footer, icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)

@bot.listen()
async def on_member_remove(member):
	guild = member.guild
	channel = guild.get_channel(638781530667352085)
	if member.bot:
		em = discord.Embed(colour=0x70702f)
		em.set_author(name="Member left!")
		em.description = f'A bot called {member.name} left our server!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text=footer, icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	else:
		em = discord.Embed(colour=0x70702f)
		em.set_author(name="Member left!")
		em.description = f'A programmer called {member.name} left our server!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text=footer, icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	
bot.run('NjM5MTY3NDAzOTAwNTM0Nzky.XhGz4g.dX0_SJ_N948tnu7cZXtONyiRNuI')