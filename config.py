import os

api_id = int(os.environ.get("API_ID", 20821267))
api_hash = os.environ.get("API_HASH", "8723cdf433be176300044547ee6bab7a")
bot_token = os.environ.get("BOT_TOKEN", "7757892840:AAHtk7qVt9r55Ovm-eYW71f1_ohNMdvUohc")
auth_users = [int(x.strip()) for x in os.environ.get("AUTH_USERS", "7894095051").split(",") if x.strip().isdigit()]

if not api_id: raise ValueError("Set API_ID env var!")
if not api_hash: raise ValueError("Set API_HASH env var!")
if not bot_token: raise ValueError("Set BOT_TOKEN env var!")
if not auth_users: raise ValueError("Set AUTH_USERS env var!")
