import discord
import lib_9gag
import lib_images
import lib_admintools
import lib_wikipedia
import lib_draemel
import lib_calc
import secrets
import sys
from discord.ext import commands

description = '''DasCord

Just one simple bot...'''

client = discord.Client()
bot = commands.Bot(command_prefix='$', description=description)


@bot.event
async def on_ready():
    sys.stderr = lib_admintools.log
    sys.stdout = lib_admintools.log
    await bot.change_presence(game=discord.Game(name='suicide'))
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('#------#')


@bot.event
async def on_message(message):
    if not message.server:
        server = "PM"
    else:
        server = message.server.name
    print(str(message.timestamp) + ' > ' + str(message.author) + '@' + str(server) + '->' + str(message.channel.name) + ': ' + str(message.content))
    # await bot.delete_message(message)
    try:
        await bot.process_commands(message)
    except Exception as err:
        await bot.say(message.channel, "OBJECTION! ...ehh EXCEPTION!: {0}".format(err))


@bot.command(pass_context=True)
async def ping(ctx):
    """...Pong"""
    await bot.add_reaction(ctx.message, '\U0001F3D3')


@bot.command()
async def issue(num: int):
    """Links to the given Github-Issue"""
    await bot.say('''Issue:
    https://github.com/das-keyboard/speedrun-the-game/issues/''' + str(num))


@bot.command(pass_context=True)
async def hot(ctx, num: int = 0):
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
async def new(ctx, num: int = 0):
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
async def sec(ctx, sec: str = "funny", num: int = 0):
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
async def img(ctx, search: str, num: int = 0):
    """Searches for an Image..."""
    if not search:
        await bot.say("Nothing to search for :(")
        return
    if num == 0:
        await bot.say(
            ctx.message.author.mention + " I searched for " + search + ". And I found this: " + lib_images.img(search,
                                                                                                               num))
    else:
        await bot.say(
            ctx.message.author.mention + " I searched for " + search + "[#" + str(
                num) + "]. And I found this: " + lib_images.img(search, num))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def i(ctx, *, search: str):
    """Searches for an Image... but much simpler."""
    if not search:
        await bot.say("Nothing to search for :(")
        return
    await bot.say(
        ctx.message.author.mention + " I searched for " + search + ". And I found this: " + lib_images.img(search, 0))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def admin(ctx, com: str = ''):
    """A set of admin tools"""
    if not ctx.message.author.id == secrets.MYID:
        await bot.say("You are not my master!")
        return
    else:
        if com == 'reload':
            msg = await bot.send_message(ctx.message.channel, 'Reloading...')
            link = lib_admintools.reload()
            if not link:
                await bot.edit_message(msg, 'Something went wrong. Abort!')
                return
            await bot.edit_message(msg, 'Done reloading: ' + link)
            await bot.send_message(ctx.message.channel, 'Restarting...')
            lib_admintools.restart()
            return
        if com == 'restart':
            await bot.send_message(ctx.message.channel, 'Restarting...')
            lib_admintools.restart()
            return
        if com == 'stop':
            await bot.send_message(ctx.message.channel, 'RIP me :(')
            lib_admintools.stop()
            return
        if com == 'log':
            await bot.send_message(ctx.message.channel, 'Listen to my Feelings:\n' + str(lib_admintools.getlog()))
            return
        await bot.send_message(ctx.message.channel, 'Command not found...')


@bot.command(pass_context=True)
async def wiki(ctx, search: str, local: str = 'de', first: int = 0):
    """Gives Wikipedia summary..."""
    await bot.say(
        ctx.message.author.mention + ' Knowledge is power! Take this: ' + lib_wikipedia.wikisum(search, local, first))
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def buy(ctx):
    data = lib_draemel.randomart()
    await bot.say(
        ctx.message.author.mention + ' You should really buy this: ' + data[0] + ' \n' + data[1])
    await bot.delete_message(ctx.message)


@bot.command(pass_context=True)
async def game(ctx, *, game: str = "No Game"):
    await bot.change_presence(game=discord.Game(name=game))
    await bot.say('I`ll play a round of ' + game + ' now. Please do not disturb!')
    await bot.delete_message(ctx.message)

@bot.command(pass_context=True)
async def calc(ctx, *, erg: str = '1 + 1'):
    await bot.say(ctx.message.author.mention + ' ' + str(erg) + ' = ' + str(lib_calc.calc(erg)))
    await bot.delete_message(ctx.message)


@bot.command()
async def loopi(*, search: str):
    if not search:
        await bot.say("Nothing to search for :(")
        return
    while True:
        await bot.say("I'm just getting started... " + lib_images.img(search, 0))

bot.run(secrets.DISCORD_KEY)
