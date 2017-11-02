import discord
import lib_9gag
import lib_images
import secrets
from discord.ext import commands

description = '''DasCord

Just one simple bot...'''

client = discord.Client()
bot = commands.Bot(command_prefix='$', description=description)
bot.change_presence(game=discord.Game(name='suicide'))


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('#------#')


@bot.event
async def on_message(message):
    print(message.content)
    #await bot.delete_message(message)
    await bot.process_commands(message)


@bot.command()
async def info():
    """Gives Information"""
    await bot.say(description)


@bot.command()
async def issue(num : int):
    """Links to the given Github-Issue"""
    await bot.say('''Issue:
    https://github.com/das-keyboard/speedrun-the-game/issues/''' + str(num))


@bot.command(pass_context=True)
async def hot(ctx, num : int = 0):
    """Posts hottest Image on 9FAG"""
    try:
        data = lib_9gag.gethottestimg(num)
    except:
        await bot.say("Something went wrong :(")
        return
    if num == 0:
        msg = " This is the hottest image from 9FAG: "
    else:
        msg = " This is the hottest image number " + str(num - 1) + "# from 9FAG: "
    await bot.say(ctx.message.author.mention + msg + str(data[0]) + '\n' + str(data[1]))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def new(ctx, num : int = 0):
    """Posts newest Image on 9FAG"""
    try:
        data = lib_9gag.getnewestimg(num)
    except:
        await bot.say("Something went wrong :(")
        return
    if num == 0:
        msg = " This is the newest image from 9FAG: "
    else:
        msg = " This is the newest image number " + str(num - 1) + "# from 9FAG: "
    await bot.say(ctx.message.author.mention + msg + str(data[0]) + '\n' + str(data[1]))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def sec(ctx, sec : str = "funny", num : int = 0):
    """Posts newest Image on 9FAG"""
    if sec == "anime-manga":
        await bot.say(ctx.message.author.mention + " " + "FUCKING WEEB! GTFO! REEEEEEEEEEEEEEEE")
        return
    try:
        data = lib_9gag.getimg(sec, num)
    except:
        await bot.say("Something went wrong :(")
        return
    if num == 0:
        msg = " This is the hottest image from your section (" + sec + "): "
    else:
        msg = " This is the hottest image number " + str(num - 1) + "# from your section (" + sec + "): "
    await bot.say(ctx.message.author.mention + msg + str(data[0]) + '\n' + str(data[1]))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def img(ctx, search: str):
    """Searches for an Image..."""
    if not search:
        await bot.say("Nothing to search for :(")
        return
    await bot.say(ctx.message.author.mention + " I searched for " + search + ". And I found this: " + lib_images.img(search))
    await bot.delete_message(ctx.message)


bot.run(secrets.DISCORD_KEY)



