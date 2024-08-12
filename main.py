import os
import discord
import requests
from dotenv import load_dotenv
import asyncio
import io

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
FAL_API_KEY = os.getenv('FAL_API_KEY')

class MyClient(discord.Client):
    def __init__(self, *, intents: discord.Intents):
        super().__init__(intents=intents)

intents = discord.Intents.default()
intents.message_content = True  # Enable message content intent
client = MyClient(intents=intents)

ALLOWED_CHANNEL_ID = 1272399269965598752

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id != ALLOWED_CHANNEL_ID:
        return

    if message.content.startswith('!generate'):
        prompt = message.content[9:].strip()  # Remove '!generate ' from the message
        if not prompt:
            await message.channel.send("Please provide a prompt after !generate")
            return

        async with message.channel.typing():
            def make_request():
                response = requests.post(
                    "https://fal.run/fal-ai/fast-lightning-sdxl",
                    headers={
                        "Authorization": f"Key {FAL_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={"prompt": prompt},
                )
                return response

            response = await asyncio.to_thread(make_request)
            prompt_details = response.json()
            if response.status_code == 200:
                image_json = prompt_details['images'][0]
                # Download the image
                image_response = requests.get(image_json['url'])
                if image_response.status_code == 200:
                    # Check if the image is NSFW
                    is_nsfw = prompt_details.get('has_nsfw_concepts', [False])[0]
                    
                    # Create a file-like object from the image content
                    image_file = discord.File(fp=io.BytesIO(image_response.content), filename="generated_image.png", spoiler=is_nsfw)
                    
                    nsfw_warning = "**[NSFW WARNING]** This image may contain sensitive content. Click to reveal." if is_nsfw else ""
                    
                    await message.channel.send(
                        f"{nsfw_warning}\nUser <@{message.author.id}> triggered image generation with prompt: {prompt_details['prompt']}\nInference time: {round(prompt_details['timings']['inference'], 3)}",
                        file=image_file
                    )
                else:
                    await message.channel.send("An error occurred while downloading the generated image.")
            else:
                await message.channel.send("An error occurred while processing your request.")

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')
    print('------')

client.run(DISCORD_TOKEN)