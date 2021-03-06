import discord
from discord.ext import commands
from discord.voice_client import VoiceClient



startup_extensions = ["Music"]
bot = commands.Bot("?")

@bot.event
async def on_ready():
    print("bot online")

class Main_Commands():
    def __init__(self, bot):
        self.bot = bot

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("pong")


@bot.command(pass_context=True)
async def hello(ctx):
    await bot.say("hi :wave:")

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '(}: (}'.format(type(e).__name__, e)
            print('Failed to load extension (}\(}'.format(extension, exc))


bot.run("NDMxNzcyMjU0NTExMTY5NTQ2.Da-dUw.cPBwwhvtBqW_dpzdhcG9NI9qvuk")

client.login(process.env.NDMxNzcyMjU0NTExMTY5NTQ2.Da-dUw.cPBwwhvtBqW_dpzdhcG9NI9qvuk);
