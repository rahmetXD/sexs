import random
import os
import logging
import asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins
from asyncio import sleep
from Config import Config
import random
import pyrogram
from youtubesearchpython import VideosSearch
import youtube_dl
import platform
from telethon.tl import types
from telethon.tl import functions, types
import telethon
from datetime import datetime
from telethon.tl import functions
import re
import requests
from bs4 import BeautifulSoup
from youtube_search import YoutubeSearch
import requests
import os
from pyrogram import filters
import os
import asyncio
import time
from telethon.sync import TelegramClient, events



logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = Config.API_ID
api_hash = Config.API_HASH
bot_token = Config.BOT_TOKEN
bot_username = Config.BOT_USERNAME
support = Config.SUPPORT_CHAT
owner = Config.OWNER_USERNAME
bot_name = Config.BOT_NAME


SUDO_USERS = Config.SUDO_USERS

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []

tekli_calisan = []

ozel_list = [1948748468]
anlik_calisan = []
grup_sayi = []
etiketuye = []
rxyzdev_tagTot = {}
rxyzdev_initT = {}



@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("👋🏻 ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴀʜʀɪ! ʙᴀᴢı ᴋᴜʟʟᴀɴışʟı ᴏ̈ᴢᴇʟʟɪᴋʟᴇʀᴇ sᴀʜɪᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴜ̈ʏᴇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ.\n\n📚 sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ!",
                    buttons=(                  
		                      
                      [Button.url('➕ɢʀᴜʙᴀ ᴇᴋʟᴇ➕', f"https://t.me/{bot_username}?startgroup=a")],
                      [Button.url('📣ᴅᴇsᴛᴇᴋ📣', f"https://t.me/{support}")],
                      [Button.inline("📚ᴋᴏᴍᴜᴛʟᴀʀ📚", data="help")],
                      [Button.url('🛡ᴏᴡɴᴇʀ🛡', 'https://t.me/rahmetiNC')],
		                  
                    ),
                    link_preview=False
                   )

@client.on(events.callbackquery.CallbackQuery(data="help"))
async def help(event):
    await event.edit(f"⚙️ ᴍᴇʀʜᴀʙᴀ, ɪ̇şᴛᴇ ᴋᴏᴍᴜᴛʟᴀʀıᴍ ⚙️\n\n » /tag \n - 5 ᴋɪşɪʟɪᴋ ᴇᴛɪᴋᴇᴛ ᴏʟᴜşᴛᴜʀᴜʀ. \n » /otag \n - ᴋᴜʟʟᴀɴıᴄıʟᴀʀı sᴏʀᴜʏʟᴀ ᴇᴛɪᴋᴇᴛʟᴇʀ. \n » /ctag \n - ᴋᴜʟʟᴀɴıᴄıʟᴀʀı ʜᴏş sᴏ̈ᴢʟᴇʀʟᴇ ᴇᴛɪᴋᴇᴛʟᴇʀ. \n » /etag \n - ᴇᴍᴏᴊɪ ɪ̇ʟᴇ ᴇᴛɪᴋᴇᴛ ᴀᴛᴀʀ.\n » /tektag \n - ᴜ̈ʏᴇʟᴇʀɪ ᴛᴇᴋᴇʀ ᴛᴇᴋᴇʀ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /btag \n - ʙᴀʏʀᴀᴋʟı şᴇᴋɪʟᴅᴇ ᴜ̈ʏᴇʟᴇʀɪ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /admins \n - ᴀᴅᴍɪɴʟᴇʀɪ ᴅᴜ̈ᴢᴇɴʟɪ şᴇᴋɪʟᴅᴇ ᴇᴛɪᴋᴇᴛʟᴇʀ.\n » /slap \n - ʙɪ̇ʀ ᴋᴜʟʟᴀɴɪᴄɪʏɪ ᴛʀᴏʟʟᴇʀ.\n » /eros \n - ᴇʀᴏsᴜɴ ᴏᴋᴜɴᴜ ᴀᴛᴀʀ.", buttons=(

                   
                  [
                      Button.inline("➡️ ɢᴇʀɪ", data="start")
                    ]
                 ),
               link_preview=False)    


@client.on(events.callbackquery.CallbackQuery(data="start"))
async def start(event):
    await event.edit(f"👋🏻 ᴍᴇʀʜᴀʙᴀ, ʙᴇɴ ᴀʜʀɪ! ʙᴀᴢı ᴋᴜʟʟᴀɴışʟı ᴏ̈ᴢᴇʟʟɪᴋʟᴇʀᴇ sᴀʜɪᴘ ᴛᴇʟᴇɢʀᴀᴍ ᴜ̈ʏᴇ ᴇᴛɪᴋᴇᴛʟᴇᴍᴇ ʙᴏᴛᴜʏᴜᴍ.\n\n📚 sɪᴢᴇ ʏᴀʀᴅɪᴍᴄɪ ᴏʟᴀʙɪʟᴍᴇᴍ ɪᴄ̧ɪɴ ᴀşşᴀɢ̆ɪᴅᴀᴋɪ ʙᴜᴛᴏɴʟᴀʀɪ ᴋᴜʟʟᴀɴɪɴ!", 
                 buttons=(                  
		                      
                      [Button.url('➕ɢʀᴜʙᴀ ᴇᴋʟᴇ➕', f"https://t.me/{bot_username}?startgroup=a")],
                      [Button.url('📣ᴅᴇsᴛᴇᴋ📣', f"https://t.me/{support}")],
                      [Button.inline("📚ᴋᴏᴍᴜᴛʟᴀʀ📚", data="help")],
                      [Button.url('🛡ᴏᴡɴᴇʀ🛡', 'https://t.me/rahmetiNC')],
		                  
                    ),
                    link_preview=False
                   )


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
  
  if event.chat_id in rxyzdev_tagTot:await event.respond(f"Etiket işlemi durduruldu!\n\n Etiketlenenlerin Sayısı👤: {rxyzdev_tagTot[event.chat_id]}**")


emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")

bayrak = "🏳️‍🌈 🏳️‍⚧️ 🇺🇳 🇦🇫 🇦🇽 🇦🇱 🇩🇿 🇦🇸 🇦🇩 🇦🇴 🇦🇮 🇦🇶 🇦🇬 🇦🇷 🇦🇲 🇦🇼 🇦🇺 🇦🇹 🇦🇿 🇧🇸 🇧🇭 🇧🇩  🇧🇧 🇧🇾 🇧🇪 🇧🇿 🇧🇯 🇧🇷 🇧🇼 🇧🇦 🇧🇴 🇧🇹 🇧🇲 🇻🇬 🇧🇳 🇧🇬 🇧🇫 🇧🇮 🇰🇭 🇰🇾 🇧🇶 🇨🇻 🇮🇨 🇨🇦 🇨🇲 🇨🇫 🇹🇩 🇮🇴 🇨🇳 🇨🇱 🇨🇽 🇨🇰 🇨🇩 🇨🇬 🇰🇲 🇨🇴 🇨🇨 🇨🇷 🇨🇿 🇪🇬 🇪🇹 🇪🇺 🇸🇻 🇩🇰 🇨🇮 🇭🇷 🇨🇺 🇨🇼 🇨🇾 🇪🇨 🇩🇴 🇩🇲 🇩🇯 🇬🇶 🇪🇷 🇫🇴 🇫🇰 🇫🇯 🇪🇪 🇸🇿 🇫🇮 🇬🇲 🇬🇦 🇹🇫 🇵🇫 🇬🇫 🇫🇷 🇬🇪 🇩🇪 🇬🇭 🇬🇮 🇬🇷 🇬🇱 🇬🇳 🇬🇬 🇬🇹 🇬🇺 🇬🇵 🇬🇩 🇬🇼 🇬🇾 🇭🇹 🇭🇳 🇭🇰 🇭🇺 🎌 🇮🇪 🇮🇶 🇯🇵 🇯🇲 🇮🇷 🇮🇩 🇮🇹 🇮🇱 🇮🇳 🇮🇸 🇮🇲 🇯🇪 🇯🇴 🇰🇬 🇰🇼 🇱🇷 🇱🇾 🇱🇮 🇱🇦 🇰🇿 🇰🇪 🇱🇻 🇱🇹 🇱🇺 🇱🇧 🇰🇮 🇽🇰 🇱🇸 🇲🇴 🇲🇹 🇲🇱 🇲🇻 🇲🇾 🇲🇼 🇲🇬 🇹🇷 🇹🇱 🇸🇪 🇸🇩 🇸🇧 🇸🇴 🇰🇷".split(" ")

#  güzel isimler...!!! 
cumle = ['Üzümlü kekim ✨', 'Nar çiçeği ✨', 'Papatya 🌼', 'Karanfil ✨', 'Gül 🌹', 'Ayıcık 🐻', 'Mutlu pandam 🐼', 'Ay parem ✨', 'Ballı lokmam ✨', 'Bebişim 🥰', 'Lale 🌷', 'Zambak ⚜', 'Nergis ✨', 'Sümbül ☘️', 'Nilüfer ☘️', 'Menekşe ⚜️', 'Lavanta ✨', 'Gül pare ✨', 'Reyhan 🌷', 'Kaktüs ⚜️', 'Böğürtlen ☘️', 'Orkide ☘️', 'Manolya ✨', 'Ayçiçeği ✨', 'Tweety ⚜️', 'Star ✨', 'Yonca 🍀', 'Ateş böceği ✨',]

# sorular cano
soru = ['Naber?', 'Nerelerdesin Aşko?', 'Özledimmmmm', 'İyimisin?', 'Ayıcık seniii', 'Biraz Sohbet edelim?', 'mutlumusun?', 'Nerelisin?', 'Nerdesin Pangoo?', 'Bebişimmmmm', 'Hayvan Severmisin?', 'Çiçek Severmisin?', 'Inst Verde Flowwwlaşakk', 'Ne Zamandır Telegramdasın?', 'Bıcı Bıcıı Yaparım Dalinle', 'Çalışıyormusun?', 'Evlimisin?', 'kebap Severmisin?', 'Günün Nasıl Geçti?', 'Papağan Severmisin?', 'En Sevdiğn Rapçii?', 'Sevgilin Varmı?', 'Açmısın?', 'Okuyormusun?', 'Kaçıncı Sınıfsın?', 'Karamsarmısın?', 'Duygusalmısın?', 'Kışları Severmisin?',]

@client.on(events.NewMessage(pattern="^/btag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamam İçin Bir Sebep Yazın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(bayrak)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("İşlem Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
	
@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)	

@client.on(events.NewMessage(pattern="^/etag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("**Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""





@client.on(events.NewMessage(pattern="^/ctag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(cumle)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/otag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komutu gruplar ve kanallar için geçerli!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki Mesajları Etiketlemek İçin Kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Sebep Yok!")
  else:
    return await event.respond("İşleme Başlamak için Mesaj Yazmalısın!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soru)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
       await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
       return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{random.choice(soru)}](tg://user?id={usr.id}) "
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern="^/tag ?(.*)"))
async def mentionall(event):
  global anlik_calisan
  if event.is_private:
    return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yöneticiler Kullana Bilir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki mesajları etiket işlemi için kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("İşleme Başlamak İçin Bir Mesaj Yazmalısın!")
  else:
    return await event.respond("İşleme Başlamak İçin Sebep Yok!")
  
  if mode == "text_on_cmd":
    anlik_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    anlik_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in anlik_calisan:
        await event.respond("Etiketleme İşlemi Başarıyla Durduruldu!")
        return
      if usrnum == 5:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global anlik_calisan
  anlik_calisan.remove(event.chat_id)
	

@client.on(events.NewMessage(pattern="^/eros$"))
async def eros(event):
    # Sadece grup ve kanallarda çalıştır
    if event.is_private:
        await event.respond("Bu komut yalnızca grup ve kanallarda kullanılabilir.")
        return

    users = await client.get_participants(event.chat_id, limit=200)
    
    users_list = []
    for user in users:
        if user.bot or user.deleted:
            pass
        else:
            users_list.append(user)
    count = len(users_list)
    
    first_user = users_list[random.randint(0, count - 1)]
    second_user = users_list[random.randint(0, count - 1)]
    
    if (first_user.id == 1550788256 or first_user.id == 5576614947
        or second_user.id == 5375589992 or second_user.id == 5576614947):
        await event.respond("**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@[kullanici1](tg://user?id=5053767281) ❤️ @[kullanici2](tg://user?id=5533927130)**")
    else:
        await event.respond(f"**💌 Eros'un oku atıldı.\n• Aşıklar  :\n\n@{first_user.username} ❣️ @{second_user.username}**")


@client.on(events.NewMessage(pattern='/slap'))
async def slap(event):
    if event.is_private:
        return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")

    if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        user = reply_message.sender
        if user:
            user_name = user.first_name
            slap_phrases = [
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'nin üstüne benzin döktü!",
                f"{user_name}'yi ateşe attı!",
                f"{user_name}'nin üstüne su döktü!",
                f"{user_name}'yi dondurdu!",
                f"{user_name}'nin üzerine pasta fırlattı!",
                f"{user_name}'yi Zencilere Sattı!",
                f"{user_name}'yi Turşu Kavonozuna Soktu!",
                f"{user_name}'nin Üzerine Buz Dolabı Attı!",
                f"{user_name}'nin Kafasını Duvara Sürterek Yaktı!",
                f"{user_name}'yi Ormana Kaçırdı!",
                f"{user_name}'yi Banyoda Sukast Etti!",
            ]
            slap_phrase = random.choice(slap_phrases)
            await event.respond(f"{event.sender.first_name} {slap_phrase}")
        else:
            await event.respond("Üzgünüm, kullanıcıyı bulamıyorum!")
    else:
        await event.respond("Bu komutu kullanabilmek için bir mesaja yanıt vermelisiniz!")


@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))
async def mentionall(event):
  global tekli_calisan
  if event.is_private:
    return await event.respond("Bu komut gruplar ve kanallar için geçerlidir!")
  
  admins = []
  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Bu Komutu Sadece Yetkililer Kullana Bİlir!")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Önceki mesajları etiket işlemi için kullanamıyorum.")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Başlamak için mesaj yazmalısın!")
  else:
    return await event.respond("İşleme başlamam için mesaj yazmalısın!")
  
  if mode == "text_on_cmd":
    tekli_calisan.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"**[{usr.first_name}](tg://user?id={usr.id}) \n**"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, f"{usrtxt} {msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    tekli_calisan.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in client.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) \n"
      if event.chat_id not in tekli_calisan:
        await event.respond("Etiketleme İşlemi Durduruldu!")
        return
      if usrnum == 1:
        await client.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""

@client.on(events.NewMessage(pattern='^(?i)/cancel'))
async def cancel(event):
  global tekli_calisan
  tekli_calisan.remove(event.chat_id)
	


@client.on(events.NewMessage(pattern="/dtag"))
async def start_tagging(event):
    user = await event.get_sender()
    user_first_name = user.first_name

    # Sadece gruplar ve kanallar için işlem yapın
    if isinstance(event.chat, (types.Chat, types.Channel)):
        # Grubun adminlerini alın
        admins = await client.get_participants(event.chat_id, filter=ChannelParticipantsAdmins)

        # Eğer kullanıcı grup adminlerinden biriyse devam edin
        if user in admins:
            # Hedeflenen gruptaki son aktif olan 50 kişiyi alın
            group_entity = event.chat_id
            participants = await client.get_participants(group_entity, limit=50)

            if participants:

questions = [
    "Nerdesin?",
    "Bugün hava nasıl?",
    "Favori film karakterin kim?",
    "En sevdiğin yemek nedir?",
    "Hangi kitabı en son okudun?",
    "Hangi ülkeyi ziyaret etmek istersin?",
    "En son nerede seyahat ettin?",
    "Hangi sporu seversin?",
    "En sevdiğin müzik türü nedir?",
    "Hangi hobilerin var?",
    "En son ne zaman doğa yürüyüşü yaptın?",
    "En iyi arkadaşın kim?",
    "Hangi okulda okuyorsun?",
    "Aile üyelerinin isimleri neler?",
    "Favori spor takımın kim?",
    "Hangi tarihi dönemi merak ediyorsun?",
    "Düşlediğin iş nedir?",
    "Hangi renkleri seversin?",
    "Favori hayvanın nedir?",
    "Hangi dilleri konuşuyorsun?",
    "En son ne zaman bir konserdeydin?",
    "En sevdiğin mevsim nedir?",
    "Hangi ünlüyle tanışmak istersin?",
    "En son hangi filmi izledin?",
    "Favori video oyunun nedir?",
    "En son ne zaman bir müze ziyareti yaptın?",
    "Hangi tatil destinasyonunu önerirsin?",
    # Buraya eklemek istediğiniz diğer soruları ekleyebilirsiniz.
]

                # Katılımcıları rastgele sırayla karıştırın
                random.shuffle(participants)
                for i, participant in enumerate(participants):
                    if not participant.bot and not participant.deleted:
                        username = participant.username
                        if username:
                            question = random.choice(questions)  # Rastgele bir soru seçin
                            tagged_message = f"⤇ @{username}, {question}"
                            await event.respond(tagged_message)
                            await asyncio.sleep(2)  # 2 saniye bekle
                            questions.remove(question)  # Aynı soruyu birden fazla kişiye sormamak için kaldırın
        else:
            await event.respond("Bu komutu kullanabilmek için bir grup admini olmalısınız!")
    else:
        await event.respond("Bu komut yalnızca gruplar ve kanallarda kullanılabilir!")

@client.on(events.NewMessage(pattern="/cancel"))
async def cancel_tagging(event):
    # Etiketleme işlemini iptal et
    await event.respond(
        "Etiketleme İşlemi İptal Edildi!",
        buttons=[
            [Button.url('🛡ᴏᴡɴᴇʀ🛡', 'https://t.me/rahmetiNC')]
        ]
    )

	

print("Ahri Tagger AKtif, Sağol Sahip! @rahmetiNC ✨")
client.run_until_disconnected()
