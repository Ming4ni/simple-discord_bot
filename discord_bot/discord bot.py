import discord
from discord.ext import commands
from discord.member import Member
import json

with open('setting.json','r',encoding='utf8')as jfile:
    jdata = json.load(jfile)


intents = discord.Intents.all()


client = commands.Bot(command_prefix = '*',intents = intents)

@client.event
async def on_connect():
    print("bot is online")
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(int(jdata['Welcome_member']))
    await channel.send(f"Welcome to the Server {member.mention} !")

   
@client.event
async def on_member_remove(member): 
    channel = client.get_channel(int(jdata['Leave_channel']))
    await channel.send(f"{member} Leave the Server!")

client.run(jdata['TOKEN'])