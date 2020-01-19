import discord
from discord.ext import commands

bot = commands.Bot(command_prefix=None)
emo = '<:welcomer:667276923021295626>'

@bot.event
async def on_ready():
	print(bot.user.name)
	print(bot.user.id)
	activity = discord.Activity(type=3)
	activity.name = "new members"
	await bot.change_presence(activity=activity, status=discord.Status.idle)

@bot.listen()
async def on_member_join(member):
	guild = member.guild
	channel = guild.get_channel(638781504817987597)
	if member == bot:
		devs = discord.utils.get(guild.roles, name="Developers")
		await user.edit(roles=[devs])
		em = discord.Embed(colour=0xffff00)
		em.set_author(name="Member joined!")
		em.description = f'A bot called {member.name} joined to us!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text="Programmer welcomer / Support server", icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	elif member != bot:
		devs = discord.utils.get(guild.roles, name="Developers")
		await user.edit(roles=[devs])
		em = discord.Embed(colour=0xffff00)
		em.set_author(name="Member joined!")
		em.description = f'A programmer called {member.name} joined to us!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text="Programmer welcomer / Support server", icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)

@bot.listen()
async def on_member_remove(member):
	guild = member.guild
	channel = guild.get_channel(638781530667352085)
	if member == bot:
		em = discord.Embed(colour=0x70702f)
		em.set_author(name="Member left!")
		em.description = f'A bot called {member.name} left our server!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text="Programmer welcomer / Support server", icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	elif member != bot:
		em = discord.Embed(colour=0x70702f)
		em.set_author(name="Member left!")
		em.description = f'A programmer called {member.name} left our server!'
		em.set_thumbnail(url=member.avatar_url)
		em.set_footer(text="Programmer welcomer / Support server", icon_url=bot.user.avatar_url)
		msg = await channel.send(embed=em)
		await msg.add_reaction(emo)
	
bot.run('NjM5MTY3NDAzOTAwNTM0Nzky.XhGz4g.dX0_SJ_N948tnu7cZXtONyiRNuI')