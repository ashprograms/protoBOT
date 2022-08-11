import discord

from utility.data import Bot

print("Logging in...")
print("\nYou should have recieved a copy of the MIT license with this software.\nIf not, report this to ashh_dev@protonmail.com immediately.")

bot = Bot(
    command_prefix=".", prefix=".", owner_ids=[942984874464247852], command_attrs=dict(hidden=True),
    allowed_mentions=discord.AllowedMentions(roles=False,users=True,everyone=False),
    intents=discord.Intents(
        guilds=True,members=True,messages=True,reactions=True,presences=True
    )
)

try:
    print("Logged in")
    bot.run("MTAwNzA5NDY2Nzg2NDcxMTI0OQ.GoT29Z.t3TP2zdFTRcG6eALLhlSC4rTyXPbtL3HDgiu4I")
    print("\nGoodbye!")
except Exception as e:
    print(f"Error while logging in: {e}")
