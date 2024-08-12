Goal:

Make an AI image generator bot in discord. 

DISCORD_BOT_TOKEN is what we'll need to run the bot.
Use FAL_API_KEY.
ToDos:

[]- generate a Discord bot
The bot should listen for messages in a channel and respond to them: 

/generate <prompt>

Example response should look like this:
```
{'images': 
  [
    {'url': 'https://fal.media/files/tiger/Oj5XjisXeCFnty572NfkG.jpeg', 
    'width': 1024, 
    'height': 1024, 
    'content_type': 'image/jpeg'}], 
    'timings': {'inference': 0.3648129357025027}, 
    'seed': 15097976535021680567, 
    'has_nsfw_concepts': [False], 
    'prompt': 'goldfish'
    }
    timings': {'inference': 0.3446060875430703}, 
    'seed': 15505567197332177513, 
    'has_nsfw_concepts': [False], 
    'prompt': 'pasta'
}
```

When the bot sees the message, it will take it and send it to FAL.ai.


[x] - make images channel:

make images channel:
If message is in this channel, respond to it.
1272399269965598752

[x] - add an attachment in discord instead of link.
[x] - only respond if triggered in images channel
[x] - return inference time
[x] - check for NSFW and add a spoiler CENSOR if it is.
[x] - rate limit 1 image per person per 5 minutes.
[] - add logging to server.
[] - Deploy it to PROD.

### Stretch Goals:
[] - 1/100 chance of something else.
User gets a message with 🎰 slot machine saying you triggered a random action.
It could....
[] - add a `--style` field.
[] - add a `--format` field.
[] - chaos etc.
[] - add optional field for theme. `--niji` = anime style, 
[] - add a `--aspect_ratio` field.
[] - add a `--seed` field.
[] - fields for vertical and horizontal.# discord_ai_image_gen_bot
