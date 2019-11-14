import discord
from discord.ext import commands
from discord import reaction
import asyncio
import keep_alive

class MyClient(discord.Client):
	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		print("bot online")
		
	async def on_member_join(self, member):
		guild = member.guild
		channel = self.get_channel(638781504817987597)
		if guild.channel is not None:
			to_send = 'Welcome {0.mention} to **{1.name}**, Read Our Rules!'. format(member, guild)
			await guild.channel.send(to_send)
			await add_self.emoji_reaction(data['white_check_mark'])
			
			await asyncio.gather(
			client.change_presence(activity=discord.Activity(type=4, name='People')))
			
client = MyClient()
client.run('NjM5MTY3NDAzOTAwNTM0Nzky.XbnVyg.LSaEaSSwrrbRCM3cVIwC5xVywgk')
		
