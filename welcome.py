# welcome.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = f"Hey {user.first_name} {user.last_name}" if user.last_name else f"Hey {user.first_name}"

    # বাটন তৈরি
    keyboard = [
        [
            InlineKeyboardButton("🛠 Menu", callback_data="/menu"),
            InlineKeyboardButton("💻 Apps", callback_data="apps"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(f"{user_name}\nWelcome to Sajedur0!", reply_markup=reply_markup)
