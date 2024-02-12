# bot.py

import os
import discBot
import requests
import json
import responses
from discord import Intents, Client, Message
from discord.ext import commands
from dotenv import load_dotenv
from typing import Final

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = Intents.default()
intents.message_content = True

client=Client(intents=intents)
#client=commands.Bot(command_prefix='*', intents=intents)


async def send_message(message: Message, user_message: str) -> None:
        if not user_message:
            print('Message was empty')
            return

        if is_private:=user_message[0] == '?':
            user_message=user_message[1:]

        try:
            response: str=responses.get_response(user_message)
            await message.author.send(response) if is_private else await message.channel.send(response)
        except Exception as e:
            print(e)

@client.event
async def on_ready():
    print("Cringe has connected to Discord")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    username=str(message.author)
    user_message=message.content
    channel=str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message,user_message)



client.run('MTIwNTA3NjcyODgwNDk0MTgyNA.G9ozbI.r2RoiwY41hL3ou5q3Wy_DspQwDVO4NlB5zzrxo')


