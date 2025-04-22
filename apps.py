# apps.py
from telegram import Update
from telegram.ext import ContextTypes

async def show_apps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    await query.edit_message_text("💻 Here are some apps:\n1. App A\n2. App B")
