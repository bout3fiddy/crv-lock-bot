import asyncio
import os

import discord
from discord.ext import commands

from utils import init_contract

bot = commands.Bot(command_prefix=".")
token = os.path.join("crv_locked_bot_token")
guild_id = 820795644494610432


veCRV_contract = init_contract(
        "0x5f3b5DfEb7B28CDbD7FAba78963EE202a494e2A2"
    )
veCRV_decimals = veCRV_contract.functions.decimals().call()
convex_voterproxy_addr = "0x989AEb4d175e16225E39E87d0D97A3360524AD80"


async def send_update():

    veCRV_balance_wei = veCRV_contract.functions.locked(
        convex_voterproxy_addr
    ).call()[0]
    veCRV_balance = round(veCRV_balance_wei / 10 ** veCRV_decimals, 2)
    nickname = (
        f"{veCRV_balance:,}"
    )
    activity_status = "CRV locked"
    await bot.get_guild(guild_id).me.edit(nick=nickname)
    await bot.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=activity_status
        )
    )
    await asyncio.sleep(60)  # in seconds


@bot.event
async def on_ready():
    """
    When discord client is ready
    """
    while True:
        await send_update()


bot.run(token)
