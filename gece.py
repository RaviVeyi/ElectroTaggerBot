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
from config import client, USERNAME, log_qrup, startmesaj, qrupstart, komutlar, sahib, support

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
     await client.send_message(log_qrup, f"ℹ️ **Yeni istifadəçi -** {ad}")
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
                      Button.inline("◀️ Geri", data="start")
                      ]
                    ),
                    link_preview=False)

# 5 li etiketleme modulü
@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global gece_tag
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

anlik_calisan = []

tekli_calisan = []




emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def etag(event):
  global gece_tag
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
ctag = (
"Su qabını daşlığa aparan kimsə, onu daşdan qorumağı öyrənməlidir."
"Nə qədər bilirsənsə bil, söylədiklərin qarşındakının anlayacağı qədərdir…"
"bayaqdan səni gözləyirəm hardasan😒"
"Təəssüf ki, sən dəlisən, anormalsan, başın çatmır. Amma sənə bir sirr verim, yaxşı insanların çoxu elə olur"
"O qədərini də etməz deyə düşündüyüm hər kəs, tam olaraq da o qədərini etdi"
"Insanlar onlarsız necə xoşbəxt olduğunu görəndə, sənin üçün darıxmağa başlayacaqlar.."
"Eşqlə əlaqədar ən böyük istehza: doğru insanı səhv zamanda sevmək"
"Kişilər gözəl qadınları sevərlər, amma qadınlar sevdikləri adamı yaraşıqlı hesab edərlər."
"Ətir sevmirəm, heç də ehtiyac duymadım. Çünki mənə görə ən gözəl qoxu, sevdiyinə sarıldıqdan sonra üstündə qalan qoxudur.."
"Qəribədir insan, eyni zarafata dəfələrlə gülməz amma eyni acıya dəfələrlə ağlayar."
"Bir gün ürəyincə yaşamaq yüz il sürünə sürünə yaşamaqdan yaxşıdır. "
"Dünya hamıya çatacaq qədər böyükdür. Başqasının yerini tutmağa çalışmaqdansa, öz yerin haqqında fikirləş."
"Heç bir şey yolunda getmir əslində, sadəcə mən görməməzliyə vururam."
"Əhəmiyyətsiz saydığımız ən adi hadisələr bəzən həyatımızı cəhənnəmə döndərə bilər."
"Bəzən düşünmədən yaşamaq lazımdır, bəzən də yaşadıqlarını düşünməmək..."
"Məsafələr, sevməyi bacarmayanların bəhanəsidir..."
"Birini sevməyə başlamaq başlı başına bir iş, bir cəhddir. Güc istər, ürək istər, korluq istər. Hətta başlanğıcda elə bir an vardır ki uçurumun üstündən sıçramaq istər; düşünməyə çalışsan aşa bilməzsən on."
"Səni sevəni sevmək özünə vurğunluqdur. Səni sevməyəni sevmək, bax bu məhəbbətdir..."
"Könül almağı bacarmayana ömür əmanət edilməz."
"Bu gözəl həyat təkcə bizim deyil. Bu həqiqəti anlayıb başqalarına ziyan vermədən yaşamağı öyrənməliyik. "
"İncitmək istəmədiyim üçün susuram verecek cavabım yoxdu sanır."
"Mən sənə oyandım yenə, sən başqalarıyla yatarkən ..."
"Bilərəm, gedənlə ölünməz amma qalanlarla da yaşanmır."
"Qəlbinin nə qədər qırıldığından çox kimin qırdığı incidir insanı."
"Əsəbləşəndə susmağı öyrəndiyim gündən bəri yetkin biriyəm."
"Yaxşı davranan kişiləri ya tərk edərlər, ya da aldadırlar."
"Çox incidildiyimdə artıq sadəcə mən öyrəşmişəm deyirəm.🥺"
"Yaxşı sevgilim deyilsən, amma bu səni sevmədiyim, qısqanmadığım, darıxmadığım anlamına gəlməz, gələ bilməz."
"Səhvlərlə dolu bir həyat, heç bir şey etmədən keçirilən bir həyatdan daha şərəflidir."
"Nə çətindir, yazaraq izah etməyə çalışmaq susduqlarını."
"Qırılacaq 206 dənə sümüyünüz varkən, axmağın biri gəlir ürəyimizi qırır."
)

@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def ctag(event):
  global gece_tag
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
      usrtxt += f"[{random.choice(ctag)}](tg://user?id={usr.id}) "
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

sehidler = "Abdullayev Qəzənfər Nəcəf Abdullayev Nurlan İnqilab Abdullayev Nicat Mirnəbi Abdullayev Məhəmməd Ramazan Allahverənov Telman Fazil Alıyev Qələndər Nofəl Abdullayev İbrahim Habil Abdullayev Elşən Sabir Abdullayev Həsən Qərib󠁧󠁢󠁷󠁬󠁳󠁿󠁧󠁢󠁷󠁬󠁳󠁿".split(" ")
 
@client.on(events.NewMessage(pattern="^/sehid ?(.*)"))
async def ctag(event):
  global gece_tag
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
      usrtxt += f"[{random.choice(ctag)}](tg://user?id={usr.id}) "
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
      usrtxt += f"[{random.choice(bayraq)}](tg://user?id={usr.id}) "
      if event.chat_id not in gece_tag:
        await event.respond("⛔ Bayraq  larla Tağ Pr Dayandırıldı",
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


print(">> Bot çalışmaktadur merak etme 🚀 @mutsuz_panda bilgi alabilirsin <<")
client.run_until_disconnected()
run_until_disconnected()
