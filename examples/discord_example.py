from discord.ext import commands
import ScuffedAPI

bot = commands.Bot(
    command_prefix='_',
    case_insensitive=True
)

@bot.event
async def on_ready():
    print('Started discord bot.')
    activity = discord.Activity(name='with ScuffedAPI', type=discord.ActivityType.playing)
    await bot.change_presence(activity=activity)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.command()
async def banner(ctx, *, content:str):
    banner = await ScuffedAPI.get_banner(name=content)
    await ctx.send(banner.id)

bot.run('X')
