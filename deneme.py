# Grup içi start komutuna karşılık verilecek mesaj

@client.on(events.NewMessage(pattern="^/start$"))
async def prmsg(event: events.NewMessage.Event):
  if event.is_group:
    return await client.send_message(event.chat_id, f"Bir rol takımı seçin.",
buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurt Takımı', data='kurt'),
                       Button.inline('👤 Bireysel', data='bireysel')
                      ],
                    ),
                    link_preview=False)


# Grup içi mesajda geri dön buton fonksiyonu

@client.on(events.callbackquery.CallbackQuery(data="grstart"))
async def start(event):
    async for usr in client.iter_participants(event.chat_id):
     await event.edit(f"Bir rol takımı seçin.",
                    buttons=(
                      [
                       Button.inline('👱 Köylü Takımı', data='koylu')
                      ],
                      [
                       Button.inline('🐺 Kurt Takımı', data='kurt'),
                       Button.inline('👤 Bireysel', data='bireysel')
                      ],
                    ),
                    link_preview=False)



# Grup mesaj geri dön butonu
@client.on(events.callbackquery.CallbackQuery(data="koylu"))
async def handler(event):
    await event.edit(f"Hakkında bilgi almak istediğiniz rolü seçin.", buttons=(
                      [
                      Button.inline("Tarikat Avcısı 💂", data="tavci")
                      ],
                      [
                      Button.inline("Gözcü 👳", data="gozcu")
                      Button.inline("Sarhoş 🍻", data="sarhos")
                      ],
                      [
                      Button.inline("Yancı 💋", data="yancı")
                      Button.inline("Seyirci 👁", data="seyirci")
                      ],
                      [
                      Button.inline("Silahşör 🔫", data="silahsor")
                      Button.inline("Koruyucu Melek 👼", data="kmelek")
                      ],
                      [
                      Button.inline("Mason 👷", data="mason")
                      Button.inline("Dedektif 🕵️", data="dedektif")
                      ],
                      [
                      Button.inline("Lanetli 😾", data="lanetli")
                      Button.inline("Avcı 🎯", data="avci")
                      ],
                      [
                      Button.inline("Eros 🏹", data="eros")
                      Button.inline("Demirci ⚒️", data="demirci")
                      ],
                      [
                      Button.inline("Prens 💍", data="prens")
                      Button.inline("Muhtar 🎖", data="muhtar")
                      ],
                      [
                      Button.inline("Kahin 🌀", data="kahin")
                      Button.inline("Hükümdar 👑", data="hükümdar")
                      ],
                      [
                      Button.inline("Barışçıl ☮️", data="barışçıl")
                      Button.inline("Yaşlı Bilge 📚", data="ybilge")
                      ],
                      [
                      Button.inline("Uyutucu 💤", data="uyutucu")
                      Button.inline("Fedai 🔰", data="fedai")
                      ],
                      [
                      Button.inline("Simyacı 🍵", data="simyaci")
                      Button.inline("Güzel 💅", data="guzel")
                      ],
                      [
                      Button.inline("Fırtına Getiren 🌩", data="fırtına")
                      Button.inline("Yabanı Çocuk 👶", data="yabani")
                      ],
                      [
                      Button.inline("👈 Geri", data="grstart")
                      ]
                    ),
                    link_preview=False)
