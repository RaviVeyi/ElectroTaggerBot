import os
import heroku3
from telethon import TelegramClient, events

from pyrogram import Client
from pyrogram import filters
import logging
#
# Burayı gurcalama
# 
# 
api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")

# Telethon 
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)
#
USERNAME = os.environ.get("USERNAME")
log_qrup = int(os.environ.get("LOG_QRUP"))
startmesaj = os.environ.get("startmesaj")
komutlar = os.environ.get("komutlar")
qrupstart = os.environ.get("qrupstart")
support = os.environ.get("support")
sahib = os.environ.get("sahib")
OWNER_ID = int(os.environ.get("OWNER_ID"))
#
app = Client("GUNC",
             api_id=api_id,
             api_hash=api_hash,
             bot_token=bot_token
             )

# mutsuz_panda 
# mutsuz_panda 
# mutsuz_panda 
