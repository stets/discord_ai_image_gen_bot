export PATH="$PATH:/Users/stetsonblake/.local/pipx/venvs/ansible/bin"

source .env
ansible-playbook -i inventory.ini deploy_discord_bot.yml --extra-vars "discord_token=$DISCORD_TOKEN fal_api_key=$FAL_API_KEY"