# main.py
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler
from welcome import start
from menu import show_menu
from apps import show_apps

async def callback_handler(update, context):
    query = update.callback_query
    data = query.data

    if data == "/menu":
        await show_menu(update, context)
    elif data == "apps":
        await show_apps(update, context)
    elif data == "app1":
        await query.edit_message_text("📲 You selected App 1!")
    elif data == "back":
        await query.edit_message_text("🔙 Back to start. Use /start again.")

app = ApplicationBuilder().token("YOUR_BOT_TOKEN").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback_handler))

app.run_polling()
