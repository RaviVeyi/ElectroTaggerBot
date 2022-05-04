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


anlik_calisan = []

gece_tag = []


#tektag
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global gece_tag
  gece_tag.remove(event.chat_id)
  
  
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
                     [Button.url('📣 Söhbət Qrupu', f'https://t.me/{group}')],
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
                      Button.inline("🏠 Ana Səhifə", data="start")
                      ]
                    ),
                    link_preview=False)

# Yeni Etiraf
@client.on(events.NewMessage)
async def yeni_mesaj(event: events.NewMessage.Event):
  global mesaj
  if event.is_private:
    mesaj = str(event.raw_text)
    if not mesaj == "/help":
      await client.send_message(event.chat_id, f"{komutlar}", buttons=(
                      [
                      Button.inline("Əmrlər", data="help"),
                      ],
                      [
                      Button.inline("Geri Qayıt", data="start")
                      ]
                    ),
                    link_preview=False)
                    









# 5 li etiketleme modulü
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
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
    await client.send_message(event.chat_id, "❄️ Tağ Başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                      Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"➢ [{usr.first_name}](tg://user?id={usr.id})\n "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
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

# admin etiketleme modülü
@client.on(events.NewMessage(pattern="^/admintag ?(.*)"))
async def mentionalladmin(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
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
    await client.send_message(event.chat_id, "❄️ Admin tağ başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Admin Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# tek tek etiketleme modülü
@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def tektag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
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
    await client.send_message(event.chat_id, "❄️ Tek-tek tağ başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Teker teker Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

    

#########################

# Emoji ile etiketleme modülü
emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
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
    await client.send_message(event.chat_id, "❄️ Emoji li  Tağ başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Emoji  li Tağ işlemi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
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

#cumlelerle tag
cumle = ( 
'Deyir:nə sayanın qulu nədə saymayanın ağasıyam...Allahın qulu☺❤sözümün də ağasıyam🤞🏻🖤',
  
'Kobud deyləm...sadəcə hörmətə hörmət cavaba da cavabdı😌🤞🏻',
  
'Xowbəxt bir qadını sevməyə nə var ki,Həyatından əlini üzmüw bir qadını sev və xowbəxt elə.!Bax onda deyərəm ki,sevməyi bacarır...!!😊💔',
  
'~♡BilsəYdim Ki , SəNi BeLə TeZ itirəcəm...💔Dostun olaraq param-parça Qalardım🤞🏻🖤🌚',
  
'Mən ağlarkən yanımda yoxsansa, mən gülərkən kölgə etmə.',
  
'Çoxlu qüsurları olan insanlar qüsurları ilk növbədə başqalarında görürlər.',
  
'Sözlər yarpaqlara bənzəyir, çoxlu yarpağı olan ağac az bəhrə verir. - Aleksandr Pop',
  
'Sevgi körpü qurmaqdır. İnsanlar körpü quracaqları yerdə, divar hördükləri üçün yalnızdırlar. - İsaak Nyuton',
  
'Qadının ən böyük cavahiratı onun namusudur. - Anatol Frans',
  
'Ağıl da, qəlb də eşq atəşinin qığılcımıdır. - Məhəmməd İqbal'
  
'Kasıb da olsa, bağışlamağı bacaran zəngin insandır. - Aristotel'

'Qorxunun qulu olmaq köləliyin ən dəhşətli növüdür.',
  
'Sən belə bilməzsən, gülüşün məndə neçə bahar edər.',
  
'Sənə necə davranmalarını istəyirsənsə, sən də başqalarına elə davran. Lakin, ilk yaxşı davranışı sən et.',
  
'Kimisi gözəlim deyər sevdiyinə kimisi də özəlim. Amma sevgi nə gözəllik istər, nə də özəllik. Sevgi sadəcə ürək istər!',
  
'Əvvəlki kimi olsa eşqlər.. Qız, sevdiyi kişinin əlini tutmağa utansa. Kişi sevdiyinin gözlərinə baxmağa qıya bilməsə.',
  
'Anlamaq üçün dinləmirik, cavab vermək üçün dinləyirik.Ən böyük problemimiz də budur.'

'Həyat bağıra bağıra susmağı öyrədir insana.',

'Ya sevməyi bilmədik, ya da həddindən çox sevdik...',
)


@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def ctag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Söz ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Söz ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
 
 #########################
 
# şəhid adları ilə tağ Allah bütün Şəhidlərimizə Rəhmət Eləsin

sehid = "Abdullayev Qəzənfər Nəcəf Abdullayev Nurlan İnqilab Abdullayev Nicat Mirnəbi Abdullayev Məhəmməd Ramazan Allahverənov Telman Fazil Alıyev Qələndər Nofəl Abdullayev İbrahim Habil Abdullayev Elşən Sabir Abdullayev Həsən Qərib".split(" ")
 
@client.on(events.NewMessage(pattern="^/sehid ?(.*)"))
async def sehid(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Söz ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(sehid)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Söz ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
 
 #########################
 
#bayraq larla tağ 
bayrag = "🇦🇨 🇦🇩 🇦🇪 🇦🇫 🇦🇬 🇦🇮 🇦🇱 🇦🇴 🇦🇶 🇦🇷 🇦🇸 🇦🇹🇦🇺 🇦🇼 🇦🇽 🇦🇿 🇧🇦 🇧🇧 🇧🇩 🇧🇪 🇧🇫 🇧🇬 🇧🇭 🇧🇮🇧🇯 🇧🇱 🇧🇲 🇧🇳 🇧🇴 🇧🇶 🇧🇷 🇧🇸 🇧🇹 🇧🇻 🇧🇼 🇧🇾🇧🇿 🇨🇦 🇨🇨 🇨🇩 🇨🇫 🇨🇬 🇨🇭 🇨🇮 🇨🇰 🇨🇱 🇨🇲 🇨🇳🇨🇵 🇨🇷 🇨🇺 🇨🇻 🇨🇼 🇨🇽 🇨🇾 🇨🇿 🇩🇪 🇩🇬 🇩🇯 🇩🇰🇩🇲 🇩🇴 🇩🇿 🇪🇦 🇪🇨 🇪🇪 🇪🇬 🇪🇭 🇪🇷 🇪🇸 🇪🇹 🇪🇺🇫🇮 🇫🇯 🇫🇰 🇫🇲 🇫🇴 🇫🇷 🇬🇦 🇬🇧 🇬🇩 🇬🇪 🇬🇫 🇬🇬🇬🇭 🇬🇮 🇬🇱 🇬🇲 🇬🇳 🇬🇵 🇬🇶 🇬🇷 🇬🇸 🇬🇹 🇬🇺 🇬🇼🇬🇾 🇭🇰 🇭🇲 🇭🇳 🇭🇷 🇭🇹 🇭🇺 🇮🇨 🇮🇩 🇮🇪 🇮🇱 🇮🇲🇮🇳 🇮🇴 🇮🇶 🇮🇷 🇮🇸 🇮🇹 🇯🇪 🇯🇲 🇯🇴 🇯🇵 🇰🇪 🇰🇬🇰🇭 🇰🇮 🇰🇲 🇰🇳 🇰🇵 🇰🇷 🇰🇼 🇰🇾 🇰🇿 🇱🇦 🇱🇧 🇱🇨🇱🇮 🇱🇰 🇱🇷 🇱🇸 🇱🇹 🇱🇺 🇱🇻 🇱🇾 🇲🇦 🇲🇨 🇲🇩 🇲🇪🇲🇫 🇲🇬 🇲🇭 🇲🇰 🇲🇱 🇲🇲 🇲🇳 🇲🇴 🇲🇵 🇲🇶 🇲🇷 🇲🇸🇲🇹 🇲🇺 🇲🇻 🇲🇼 🇲🇽 🇲🇾 🇲🇿 🇳🇦 🇳🇨 🇳🇪 🇳🇫 🇳🇬🇳🇮 🇳🇱 🇳🇴 🇳🇵 🇳🇷 🇳🇺 🇳🇿 🇴🇲 🇵🇦 🇵🇪 🇵🇫 🇵🇬🇵🇭 🇵🇰 🇵🇱 🇵🇲 🇵🇳 🇵🇷 🇵🇸 🇵🇹 🇵🇼 🇵🇾 🇶🇦 🇷🇪🇷🇴 🇷🇸 🇷🇺 🇷🇼 🇸🇦 🇸🇧 🇸🇨 🇸🇩 🇸🇪 🇸🇬 🇸🇭 🇸🇮🇸🇯 🇸🇰 🇸🇱 🇸🇲 🇸🇳 🇸🇴 🇸🇷 🇸🇸 🇸🇹 🇸🇻 🇸🇽 🇸🇾🇸🇿 🇹🇦 🇹🇨 🇹🇩 🇹🇫 🇹🇬 🇹🇭 🇹🇯 🇹🇰 🇹🇱 🇹🇲 🇹🇳🇹🇴 🇹🇷 🇹🇹 🇹🇻 🇹🇼 🇹🇿 🇺🇦 🇺🇬 🇺🇲 🇺🇳 🇺🇸 🇺🇾🇺🇿 🇻🇦 🇻🇨 🇻🇪 🇻🇬 🇻🇮 🇻🇳 🇻🇺 🇼🇫 🇼🇸 🇽🇰 🇾🇪🇾🇹 🇿🇦 🇿🇲 🇿🇼".split(" ")
 
 
@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def btag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
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
    await client.send_message(event.chat_id, "❄️ Bayraq larla  Tağ başladı\n⏱️ İnterval - 2 saniyə",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrag)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Bayraq  larla Tağ Prosesi Dayandırıldı",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
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
renk = "🔴 🟠 🟡 🟢 🔵 🟣 🟤 ⚫ ⚪ " .split(" ") 
        

@client.on(events.NewMessage(pattern="^/rtag ?(.*)"))
async def rtag(event):
  global gece_tag
  if event.is_private:
    return await event.respond(f"😡 Bu Əmri Qrupda İşlət")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond(f"Sən Admin Deyilsən 🤣")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("__Eski mesajları göremiyorum! (bu mesaj beni gruba eklemeden önce yazılmış)__")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("__Etiketleme mesajı yazmadın!__")
  else:
    return await event.respond("__Etiketleme için bir mesajı yanıtlayın veya bir mesaj yazın!__")
    
  if mode == "text_on_cmd":
    await client.send_message(event.chat_id, "❄️ Renk ile etiketleme başladı\n⏱️ İnterval - 2 saniye",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  ) 
    gece_tag.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(renk)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Renk ile etiketleme işlemi durduruldu",
                    buttons=(
                      [
                       Button.url('📣 Support', f'https://t.me/{support}')
                      ]
                    )
                  )
        return
      if usrnum == 3:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""



###############################


print(">> Bot Super İşləyir 😎 <<")
client.run_until_disconnected()
run_until_disconnected()
