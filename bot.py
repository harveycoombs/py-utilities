# Written in Python/discord.py by Harvey - @harvey-x86 - harveycoombs.com
import asyncio
import discord
import random
import time
from discord.ext import commands

client = commands.Bot(command_prefix='.', help_command=None)
embedColor = 0x2b84ff
procStart = time.time()

@client.event
async def on_ready():
    print("Bot is ready.")
    await client.change_presence(activity=discord.Activity(name=".help", type=discord.ActivityType.listening))

@client.event
async def on_server_join(member):
    joinEmbed=discord.Embed(title=f"{member} Just joined the server!")
    joinEmbed.set_footer(text=f"{member.guild} now has {member.guild.member_count} members")

    await member.guild.system_channel.send(joinEmbed)

@client.event
async def on_command_error(ctx, error):
    await ctx.send(':warning: Command Not Found. Try `.help` for a list of **existing** commands.')
    print(error)

@client.command()
async def help(ctx):
    helpEmbed=discord.Embed(title='Type `.` & then a command name', color=embedColor)
    helpEmbed.set_author(icon_url=client.user.avatar_url, name="List of current commands:")
    helpEmbed.add_field(name="`help`, `avatar`, `user`, `server`, `echo`, `crole`, `info`", value="")

    await ctx.send(embed=helpEmbed)

@client.command()
async def user(ctx, member: discord.Member):

    createDate = member.created_at.strftime("%B %d %Y")
    joinDate = member.joined_at.strftime("%B %d %Y")
    nickname = ""

    if not member.nick:
        nickname = "No nickname"
    else:
        nickname = member.display_name

    userEmbed=discord.Embed(title=f"Information for {member.name}:", color=embedColor)
    userEmbed.set_thumbnail(url=member.avatar_url)
    userEmbed.add_field(name=":label: Username:", value=member, inline=False)
    userEmbed.add_field(name=":information_source: ID:", value=member.id, inline=False)
    userEmbed.add_field(name=":date: Account Created:", value=createDate, inline=False)
    userEmbed.add_field(name=":shield: Joined Server:", value=joinDate, inline=False)
    userEmbed.add_field(name=":placard: Server Nickname?", value=nickname, inline=False)

    await ctx.send(embed=userEmbed)

@client.command()
async def server(ctx):

    guildCreateDate = ctx.guild.created_at.strftime("%B %d %Y")

    serverEmbed=discord.Embed(title=f"Information for {ctx.guild.name}:", color=embedColor)
    serverEmbed.set_thumbnail(url=ctx.guild.icon_url)
    serverEmbed.add_field(name=":label: Server Name:", value=ctx.guild.name, inline=False)
    serverEmbed.add_field(name=":information_source: ID:", value=ctx.guild.id, inline=False)
    serverEmbed.add_field(name=":date: Server Created:", value=guildCreateDate, inline=False)
    serverEmbed.add_field(name=":busts_in_silhouette: Member Count:", value=str(ctx.guild.member_count), inline=False)
    serverEmbed.add_field(name=":placard: Server Owner", value=str(ctx.guild.owner), inline=False)

    await ctx.send(embed=serverEmbed)

@client.command()
async def echo(ctx, *args):

    space = ' '
    for i in range(int(args[-1])):
        await ctx.send(space.join(args))

@client.command()
async def avatar(ctx, member: discord.Member):

    aviEmbed=discord.Embed(title=f"{member}'s avatar:", color=embedColor)
    aviEmbed.set_image(url=member.avatar_url)
    await ctx.send(embed=aviEmbed)

@client.command()
async def crole(ctx, *args):

    arguments = list(args)
    hexColorInt = int(arguments[-1], 16)
    space = ' '
    roleName = space.join(tuple(arguments[:-1]))

    crEmbed=discord.Embed(title="Role successfully created:", color=hexColorInt)
    crEmbed.add_field(name=":label: Role name:", value=f"`{roleName}`", inline=False)
    crEmbed.add_field(name=":art: Role color (Hex):", value=f"`{arguments[-1]}`", inline=False)
    crEmbed.set_footer(text=f"role created by {ctx.author}")

    await ctx.guild.create_role(name=roleName, color=discord.Color(hexColorInt))
    await ctx.send(embed=crEmbed)

@client.command()
async def info(ctx):

    timeFetch = time.time() - procStart
    uptime = "{0:.2f}ms".format(timeFetch)

    infoEmbed=discord.Embed(title=f"Bot Information:")
    infoEmbed.add_field(name=":label: Username:", value=client.user, inline=True)
    infoEmbed.add_field(name=":information_source: ID:", value=client.user.id, inline=True)
    infoEmbed.add_field(name=":tools: Developed by:", value="harvey-x86", inline=True)
    infoEmbed.add_field(name=":pencil: Written in:", value="Python", inline=True)
    infoEmbed.add_field(name=":alarm_clock: Uptime:", value=uptime, inline=True)
    infoEmbed.add_field(name=":shield: Server(s):", value=len(client.guilds), inline=True)
    infoEmbed.set_footer(text="github.com/harvey-x86")

    await ctx.send(embed=infoEmbed)

client.run("BOT_TOKEN")
