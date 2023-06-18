import discord
from discord.ext import commands
import openai

# OpenAI API credentials
openai.api_key = 'OPENAI_APIKEY'

# Discord bot setup
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

# Event to run when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Event to handle incoming messages
@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Generate a response using ChatGPT
    response = generate_response(message.content)

    # Send the response back to the Discord channel
    await message.channel.send(response)

    # Allow commands to be processed as well
    await bot.process_commands(message)

# Function to generate a response using ChatGPT
def generate_response(message):
    # Send the user's message to ChatGPT for processing
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=message,
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Run the bot
bot.run('DISCORD_BOT_TOKEN')
