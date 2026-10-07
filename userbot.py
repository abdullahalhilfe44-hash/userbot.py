import os
from telethon import TelegramClient

api_id = 2040
api_hash = "b18441a1ff607e10a989891a5462e627"
string_session = os.environ.get("SESSION", "")

client = TelegramClient(string_session, api_id, api_hash)

async def main():
    print("تم تشغيل البوت بنجاح على GitHub Actions!")

if __name__ == "__main__":
    with client:
        client.loop.run_until_complete(main())
            
