#!/bin/bash

# Add Ansible to PATH
export PATH="$PATH:/Users/stetsonblake/.local/pipx/venvs/ansible/bin"

# Source environment variables
source .env

# Run Ansible playbook with vault password file
ansible-playbook -i inventory.ini deploy_discord_bot.yml \
  --vault-password-file .vault_pass \
  --extra-vars "discord_token=$DISCORD_TOKEN fal_api_key=$FAL_API_KEY"