# Discord AI Image Generator Bot

This Discord bot generates AI images based on user prompts using FAL.ai's image generation API.

## Features

- Generates images from text prompts
- Responds to commands in a designated channel
- Attaches generated images directly to Discord messages
- Implements rate limiting (1 image per user per 5 minutes)
- Adds spoiler tags to potentially NSFW content

## Setup

1. Clone the repository
2. Install dependencies (list them in a `requirements.txt` file)
3. Set up environment variables:
   - `DISCORD_BOT_TOKEN`: Your Discord bot token
   - `FAL_API_KEY`: Your FAL.ai API key

## Usage

1. Invite the bot to your Discord server
2. Use the command `/generate <prompt>` in the designated images channel

Example:
`/generate a majestic tiger in a forest`


## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Implement your changes
4. Submit a pull request

## To-Do

- [ ] Add logging to server
- [ ] Implement secure deployment without password
- [ ] Set up automatic deployment on git push

## Stretch Goals

- [ ] Add random actions (1/100 chance)
- [ ] Implement additional command options:
  - `--style`
  - `--format`
  - `--niji` (anime style)
  - `--aspect_ratio`
  - `--seed`

## Running Locally

1. Set up your environment variables
2. Run the main bot script (provide the filename)

## Deployment

(Add instructions for deploying the bot to a production environment)

TODOS:

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

[x] - make images channel:
[x] - add an attachment in discord instead of link.
[x] - only respond if triggered in images channel
[x] - return inference time
[x] - check for NSFW and add a spoiler CENSOR if it is.
[x] - rate limit 1 image per person per 5 minutes.
[x] - Deploy it to PROD.
[] find out how to deploy without a password but still encrypt the vault.
use ssh key????

### Stretch Goals:
[] deploy to prod on git push.
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
