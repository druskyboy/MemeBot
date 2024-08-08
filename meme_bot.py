import discord
import requests

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

TOKEN = 'YOUR_BOT_TOKEN'

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!meme'):
        meme = get_meme()
        await message.channel.send(meme)
    
    elif message.content.startswith('!help'):
        help_message = (
            "**Here are the commands you can use:**\n"
            "`!meme` - Fetches a random meme from the internet.\n"
            "`!help` - Shows this help message."
        )
        await message.channel.send(help_message)

def get_meme():
    url = "https://meme-api.com/gimme"
    try:
        response = requests.get(url)
        response.raise_for_status()
        json_data = response.json()
        return json_data["url"]
    except requests.exceptions.RequestException as e:
        print(f"Error fetching meme: {e}")
        return "Sorry, I couldn't fetch a meme at this time."

client.run(TOKEN)
