import os

class Config(object):
  API_ID = int(os.environ.get("API_ID", "16536417"))
  API_HASH = os.environ.get("API_HASH", "f6e58a549da642d7b765744a2f82c6d9")
  BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
  BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
  DB_CHANNEL = int(os.environ.get("DB_CHANNEL", ""))
  SHORTLINK_URL = os.environ.get('SHORTLINK_URL', "tnshort.net")
  SHORTLINK_API = os.environ.get('SHORTLINK_API', "0a5a63bf9c2e9eb228e522930f83c516358187f6")
  BOT_OWNER = int(os.environ.get("BOT_OWNER", "921365334"))
  DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://trumbot:trumbot@cluster0.cfkaeno.mongodb.net/?retryWrites=true&w=majority")
  UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "https://t.me/The_Silent_Teams")
  LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001983863101"))
  BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
  FORWARD_AS_COPY = bool(os.environ.get("FORWARD_AS_COPY", True))
  BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", True))
  BANNED_CHAT_IDS = list(set(int(x) for x in os.environ.get("BANNED_CHAT_IDS", "").split()))
  OTHER_USERS_CAN_SAVE_FILE = bool(os.environ.get("OTHER_USERS_CAN_SAVE_FILE", True))
  ABOUT_BOT_TEXT = f"""
This is a Permanent FileStore Bot. 
Send Me any Media or File. I can Work In Channel too. Add Me to Channel with Edit Permission, I will add save Uploaded File in Channel and Share a Shareable Link. 

╭────[ 🔅FɪʟᴇSᴛᴏʀᴇBᴏᴛ🔅]────⍟
│
├🔸 My Name: [File Delivery Bot](https://t.me/{BOT_USERNAME})
│
├🔸 Language: [Python 3](https://www.python.org)
│
├🔹 Updates: [The Silent Team](https://t.me/The_Silent_Teams)
│
╰──────[ 😎 ]───────────⍟
"""
  ABOUT_DEV_TEXT = f"""
🧑🏻‍💻 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿: [ Unknown ](https://t.me/searchingshiv)
 
 I am Super noob...

[Donate Me](https://t.me/THE_DS_OFFICIAL)
"""
  HOME_TEXT = """
Hello, [{}](tg://user?id={})\n\nThis is a Permanent **File Delivery Bot**.

How to Use Bot & it's Benefits??

📢 Send me any File & It will be uploaded in My Database & You will Get the File Link.

⚠️ Benefits: If you have a TeleGram Movie Channel or Any Copyright Channel, Then Its Useful for Daily Usage, You can Send Me Your File & I will Send Permanent Link to You & Channel will be Safe from **CopyRight Infringement** Issue. I support Channel Also You Can Check **About Bot**.
"""
