from flask import Flask, request
from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup
import os

app = Flask(__name__)

TOKEN = os.environ.get("BOT_TOKEN")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")
bot = Bot(token=TOKEN)

@app.route('/')
def index():
    return "Bot is Running!"

@app.route(f'/{TOKEN}', methods=['POST'])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    
    if update.message:
        user = update.message.from_user
        chat_id = update.message.chat_id
        text = update.message.text

        # ইউজারনেম বানানো
        full_name = f"{user.first_name or ''} {user.last_name or ''}".strip()
        user_name = f"Hey {full_name}"

        # স্বাগতম মেসেজ
        welcome = f"{user_name}\nWelcome to Sajedur0!"
        bot.send_message(chat_id=chat_id, text=welcome)

        # ইনলাইন বাটন (Tools, Code, Website)
        keyboard = [
            [
                InlineKeyboardButton("🛠 Tools", callback_data='/tools'),
                InlineKeyboardButton("💻 Code", callback_data='/code'),
                InlineKeyboardButton("🌐 Website", url='https://srr0.blogspot.com')
            ]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        bot.send_message(chat_id=chat_id, text="⤵️ Choose an option:", reply_markup=reply_markup)

        # যদি /getfile কমান্ড থাকে
        if text and text.startswith('/getfile'):
            try:
                file_number = text.split(' ')[1]
                file_url = f"https://t.me/Sajedur0Server/{file_number}?single"
                caption = f"📂 **File {file_number}**\nStay with @Sajedur0"
                bot.send_document(chat_id=chat_id, document=file_url, caption=caption, parse_mode='Markdown')
            except IndexError:
                bot.send_message(chat_id=chat_id, text="⚠️ File number দিন। উদাহরণ: /getfile 2")

        # ফাইল তালিকা দেখানোর কমান্ড
        if text == "/files":
            buttons = [
                [InlineKeyboardButton("1 - Fonts", callback_data="/getfile 2")],
                [InlineKeyboardButton("All Fonts", callback_data="/getfile 3")],
                [InlineKeyboardButton("Arabic Fonts", callback_data="/getfile 4")],
                [InlineKeyboardButton("Bangla Fonts", callback_data="/getfile 5")],
                [InlineKeyboardButton("Bijoy Stylish Fonts", callback_data="/getfile 6")],
                [InlineKeyboardButton("Adobe Patch", callback_data="/getfile 7")],
                [InlineKeyboardButton("Creative Cloud Uninstaller x64", callback_data="/getfile 8")],
                [InlineKeyboardButton("Creative Cloud Uninstaller x86", callback_data="/getfile 9")],
                [InlineKeyboardButton("Lan Driver Full Package", callback_data="/getfile 10")],
                [InlineKeyboardButton("Tende Driver", callback_data="/getfile 11")],
                [InlineKeyboardButton("TP-LINK Driver", callback_data="/getfile 12")],
                [InlineKeyboardButton("Office 365 ProPlus Online Installer", callback_data="/getfile 13")],
                [InlineKeyboardButton("WinRAR v6.11", callback_data="/getfile 14")],
                [InlineKeyboardButton("Printer Fix Error", callback_data="/getfile 15")],
                [InlineKeyboardButton("Office Uninstaller", callback_data="/getfile 16")],
                [InlineKeyboardButton("Google Drive Uninstaller", callback_data="/getfile 17")],
                [InlineKeyboardButton("File 18", callback_data="/getfile 18")],
                [InlineKeyboardButton("File 19", callback_data="/getfile 19")],
                [InlineKeyboardButton("File 20", callback_data="/getfile 20")],
                [InlineKeyboardButton("File 21", callback_data="/getfile 21")],
                [InlineKeyboardButton("File 22", callback_data="/getfile 22")],
                [InlineKeyboardButton("File 23", callback_data="/getfile 23")],
                [InlineKeyboardButton("File 24", callback_data="/getfile 24")],
                [InlineKeyboardButton("File 25", callback_data="/getfile 25")],
                [InlineKeyboardButton("File 26", callback_data="/getfile 26")],
                [InlineKeyboardButton("File 27", callback_data="/getfile 27")],
                [InlineKeyboardButton("File 28", callback_data="/getfile 28")],
                [InlineKeyboardButton("File 29", callback_data="/getfile 29")],
                [InlineKeyboardButton("File 30", callback_data="/getfile 30")],
            ]
            reply_markup = InlineKeyboardMarkup(buttons)
            bot.send_message(chat_id=chat_id, text="📂 **Select a file:**", reply_markup=reply_markup, parse_mode='Markdown')

    return 'ok'

if __name__ == '__main__':
    bot.set_webhook(url=f"{WEBHOOK_URL}/{TOKEN}")
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
