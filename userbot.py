import os
from telethon import TelegramClient, events
from telethon.sessions import StringSession

API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"
SESSION_STRING = os.environ.get("SESSION", "")

if not SESSION_STRING:
    print("خطأ: لم يتم العثور على متغير SESSION أو أنه فارغ!")
    exit(1)

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    me = await client.get_me()
    print(f"البوت يعمل الآن ومستمر في الاستماع باسم: {me.first_name} (@{me.username})")

# مثال على أمر بسيط يستجيب له البوت (يمكنك إضافة أوامر الـ Userbot الخاصة بك هنا)
@client.on(events.NewMessage(pattern='.صم', outgoing=True))
async def handler(event):
    await event.edit("أهلاً بك، أنا أعمل بنجاح على GitHub Actions! 🚀")

with client:
    client.loop.run_until_complete(main())
    # هذا السطر يمنع البوت من الإغلاق ويجعله شغالاً بشكل دائم
    client.run_until_disconnected()
