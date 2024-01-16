import discord
import os
import search_function
from dotenv import load_dotenv

#Use the python-dotenv pakcage to get variables stored in .env file of your project
load_dotenv()

#instantiates discord client
client = discord.Client()

intro_message = 'Hello! Young lady'
no_result_message = 'No results'

#instantiate the runweb class
runweb = search_function.RunWeb()


#discord event to check when the bot is online
@client.event
async def on_ready():
  print('{client.user} is now online!')

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  message_content = message.content.lower()

  if message.content.startswith(f'$hello'):
    await message.channel.send(intro_message)
  
  if f'$search' in message_content:
  
    key_words, search_words = runweb.key_words_search_words(message_content)
    result_links = runweb.search(key_words)
    links = runweb.send_link(result_links, search_words)
  
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)



#retrieves bot token from .env file and runs client
client.run(os.getenv('TOKEN'))
