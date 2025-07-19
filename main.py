import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Constants
WELCOME_CHANNEL_ID = 638781504817987597
GOODBYE_CHANNEL_ID = 638781530667352085
MEMBER_ROLE_ID = 668392530542329856
BOT_ROLE_ID = 668393208438456332
EMOJI = '<:welcomer:667276923021295626>'
FOOTER_TEXT = "Programmer welcomer / Support server"

# Intents setup
intents = discord.Intents.default()
intents.members = True  # Needed for member join/leave events

# Bot initialization
bot = commands.Bot(command_prefix=None, intents=intents)

# Activity setup
@bot.event
async def on_ready():
    print(f"{bot.user} is online.")
    activity = discord.Activity(
        type=discord.ActivityType.watching, name="new members!"
    )
    await bot.change_presence(activity=activity, status=discord.Status.idle)

# Embed builder utility
def create_embed(title: str, description: str, avatar_url: str, color: discord.Colour) -> discord.Embed:
    embed = discord.Embed(title=title, description=description, colour=color)
    embed.set_thumbnail(url=avatar_url)
    embed.set_footer(text=FOOTER_TEXT, icon_url=bot.user.avatar.url)
    return embed

# Welcome handler
@bot.event
async def on_member_join(member: discord.Member):
    guild = member.guild
    channel = guild.get_channel(WELCOME_CHANNEL_ID)

    role_id = BOT_ROLE_ID if member.bot else MEMBER_ROLE_ID
    role = guild.get_role(role_id)
    await member.add_roles(role)

    label = "bot" if member.bot else "programmer"
    desc = f"A {label} called **{member.name}** joined us!"
    embed = create_embed("Member joined!", desc, member.display_avatar.url, discord.Colour.gold())

    if channel:
        msg = await channel.send(embed=embed)
        await msg.add_reaction(EMOJI)

# Goodbye handler
@bot.event
async def on_member_remove(member: discord.Member):
    guild = member.guild
    channel = guild.get_channel(GOODBYE_CHANNEL_ID)

    label = "bot" if member.bot else "programmer"
    desc = f"A {label} called **{member.name}** left our server!"
    embed = create_embed("Member left!", desc, member.display_avatar.url, discord.Colour.dark_gold())

    if channel:
        msg = await channel.send(embed=embed)
        await msg.add_reaction(EMOJI)

# Run bot securely using environment variable
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

if TOKEN:
    bot.run(TOKEN)
else:
    print("⚠️ Error: DISCORD_BOT_TOKEN not set in environment. :(")
