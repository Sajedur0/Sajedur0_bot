# menu.py
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ContextTypes

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    keyboard = [
        [InlineKeyboardButton("📱 App 1", callback_data="app1")],
        [InlineKeyboardButton("🔙 Back", callback_data="back")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text("🛠 Menu Options:", reply_markup=reply_markup)
