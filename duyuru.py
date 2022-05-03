### broadcast modülü


ozel_list = [5074483091]
anlik_calisan = []
grup_sayi = []





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