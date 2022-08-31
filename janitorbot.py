import discord
import os
import requests
import json
import random 

client = discord.Client()

m_words = [
  "blaming", 
  'fault', 
  'good', 
  'nope', 
  'psycho',
  'I swear'
]

meme_machine = [
  'Shut up',
  "Oh god",
  'You annoy me',
  'That is not my job',
  'You damn kids',
]

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + '-' + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  msg = message.content

  if msg.startswith('!test'):
    await message.channel.send ('This is a Test message')

  if msg.startswith('!hello'):
    await message.channel.send ('Hello, how may I help you?')

  if msg.startswith('!quote'):
    quote = get_quote()
    await message.channel.send(quote)
  
  if any(word in msg for word in m_words):
    await message.channel.send(random.choice(meme_machine))

client.run('token')
   