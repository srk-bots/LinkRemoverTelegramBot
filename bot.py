# main.py

from telebot import TeleBot

# config
import os

TOKEN = os.environ.get("BOT_TOKEN", "7893848371:AAHHL3GBp0mMJsdio4LybsIHlAGLKkFrBq8")
ADMINS = [int(id) for id in os.environ.get("ADMINS", "1416841137").split(',')]

# setup
app = TeleBot(TOKEN)

def check_message(type, message):
    print("\n\n\n\n==============\n\n\n")
    print(type, message)

    if message.from_user.id in ADMINS:
        return

    chat_member = app.get_chat_member(message.chat.id, message.from_user.id)
    print("==================> User data:", chat_member)
    if chat_member.status in ['creator', 'administrator']:
        return
    if chat_member.status == 'left' and chat_member.user.username == 'GroupAnonymousBot':
        return

    text = message.text or ""
    if '@' in text:
        print("Found username in message text")
        app.delete_message(message.chat.id, message.message_id)
    elif 't.me' in text or 'http://' in text or 'https://' in text or '.com' in text or '.ir' in text:
        print("Found link in message text")
        app.delete_message(message.chat.id, message.message_id)

@app.edited_message_handler(func=lambda message: True)
def edit_message(message):
    check_message("edit", message)

@app.message_handler(func=lambda message: True)
def new_message(message):
    check_message("new", message)

if __name__ == '__main__':
    app.infinity_polling()
