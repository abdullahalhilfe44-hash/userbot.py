import os
from telethon import TelegramClient
from telethon.sessions import StringSession

# معلومات التطبيق الخاصة بك
API_ID = 2040
API_HASH = "b18441a1ff607e10a989891a5462e627"

# قراءة جلسة String Session من متغيرات النظام (GitHub Secrets)
SESSION_STRING = os.environ.get("SESSION", "")

# التحقق من أن الجلسة موجودة وليست فارغة
if not SESSION_STRING:
    print("خطأ: لم يتم العثور على متغير SESSION أو أنه فارغ!")
    exit(1)

# إنشاء عميل تليثون باستخدام الجلسة المخزنة
client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

async def main():
    # كود البوت الخاص بك يكتب هنا
    me = await client.get_me()
    print(f"تم تسجيل الدخول بنجاح باسم: {me.first_name} (@{me.username})")

with client:
    client.loop.run_until_complete(main())
