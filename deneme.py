# Grup içi start komutuna karşılık verilecek mesaj

@client.on(events.NewMessage(pattern="^/start$"))
async def prmsg(event: events.NewMessage.Event):
  if event.is_group:
    return await client.send_message(event.chat_id, f"{qrupstart}",
buttons=(
                      [
                       Button.inline('📮 Komutlar ', data='grkomut'),
                       Button.url('👨🏻‍💻 Sahibim', f'https://t.me/{sahib}')
                      ],
                    ),
                    link_preview=False)


# Grup içi mesajda geri dön buton fonksiyonu

@client.on(events.callbackquery.CallbackQuery(data="grstart"))
async def start(event):
    async for usr in client.iter_participants(event.chat_id):
     await event.edit(f"{qrupstart}",
                    buttons=(
			[
                       Button.inline('📮 Komutlar ', data='grkomut'),
                       Button.url('👨🏻‍💻 Sahibim', f'https://t.me/{sahib}')
                      ],
                    ),
                    link_preview=False
                   )



# Grup mesaj geri dön butonu
@client.on(events.callbackquery.CallbackQuery(data="grkomut"))
async def handler(event):
    await event.edit(f"{komutlar}", buttons=(
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)
