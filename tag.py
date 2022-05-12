#################################
# Electro Tagger Bot #
#################################
#  Sahib - @HuseynH 
# Reponu Öz Adına Çıxaran Peysərdi
# Reponu Açığ Görüm Oğurlama Oğlum
##################################
import heroku3
import random
import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.events import StopPropagation
from config import client, USERNAME, startmesaj, qrupstart, komutlar, sahib, support, group

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)


ozel_list = [5074483091]
anlik_calisan = []
grup_sayi = []

Husu_tag = []
  
  
  
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event): 
  global Husu_tag 
  Husu_tag.remove(event.chat_id)

  
@client.on(events.callbackquery.CallbackQuery(data="cancel"))
async def cancel(event):
  global Husu_tag
  Husu_tag.remove(event.chat_id)
  
  
  
# Başlanğıc Mesajı
@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  if event.is_private:
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     return await event.reply(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Əmrlər", data="help")
                      ],
                      [Button.url('🌱 Məni Qrupa Əlavə Et', f'https://t.me/{USERNAME}?startgroup=a')],
                     [Button.url('🥳 Söhbət Qrupu', f'https://t.me/{group}')],
                      [Button.url('📣 Kanal', f'https://t.me/{support}')],
                       [Button.url('👨🏻‍💻 Sahib', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)
                    
                    
  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}")


# Başlanğıc Button
@client.on(events.callbackquery.CallbackQuery(data="start"))
async def handler(event):
    async for usr in client.iter_participants(event.chat_id):
     ad = f"[{usr.first_name}](tg://user?id={usr.id}) "
     await event.edit(f"{ad} {startmesaj}", buttons=(
                      [
                       Button.inline("✍ Əmrlər", data="help")
                      ],
                      [Button.url('🌱 Məni Qrupa Əlavə Et', f'https://t.me/{USERNAME}?startgroup=a')],
                     [Button.url('📣 Söhbət Qrupu', f'https://t.me/{group}')],
                      [Button.url('📣 Kanal', f'https://t.me/{support}')],
                       [Button.url('👨🏻‍💻 Sahib', f'https://t.me/{sahib}')]
                    ),
                    link_preview=False)
# gece kusu
@client.on(events.callbackquery.CallbackQuery(data="help"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.inline("Geri Qayıt", data="start")
                      ]
                    ),
                    link_preview=False)
                    
# 5 li tağ modulu
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def tag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ 5-li Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"🥳dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Tək Tək Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
    
#########################

# renk ile etiketleme modülü
reng = "🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
  global Husu_tag
  if event.is_private:
    return await event.respond(f"{noqrup}")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"{noadmin}")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Köhnə mesajları görə bilmirəm! (bu mesaj məni qrupa əlavə etməmişdən qabaq yazılıb)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Tağ mesajı yazmadın!__")
  else:
    return await event.respond("__Tağ etməy üçün bir mesaj yanıtlayın və ya bir mətn yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Rənglərlə Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.inline(f"dayandir", data="cancel")
                      ]
                    )
                  ) 
    Husu_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(reng)}](tg://user?id={usr.id}) "
      if event.chat_id not in Husu_tag:
        await event.respond("⛔ Rənglərlə Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                      Button.inline(f"🙄Təmirdə", data="yeniden")
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

###broadcast

@client.on(events.NewMessage(pattern='^/broadcast?(.*)'))
async def duyuru(event):
 
  global grup_sayi,ozel_list
  sender = await event.get_sender()
  if sender.id not in ozel_list:
    return
  reply = await event.get_reply_message()
  await event.respond(f"Cəmi {len(grup_sayi)} Qrupa mesaj göndərilir...")
  for x in grup_sayi:
    try:
      await client.send_message(x,f"**📣 Sponsor**\n\n{reply.message}")
    except:
      pass
  await event.respond(f"Gönderildi.")


#### botcum modülü

@app.on_message(filters.user(5074483091) & filters.command(["sahib"], ["."]))
def admin(_, message: Message):
    message.reply(f"__Sevimli Sahibim Gəldi Xoş gəldiniz Cənab 💋 Muck__")


###############################


print(">> Bot Super İşləyir 😎 <<")
client.run_until_disconnected()
run_until_disconnected()
