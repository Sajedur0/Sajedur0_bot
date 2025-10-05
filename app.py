import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# বটের টোকেন
BOT_TOKEN = "7841530700:AAETQrppsCGhL_IQM_qCvWPPs8U9yJWMQlg"

# লগিং কনফিগারেশন
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    user_name = f"Hey {user.first_name} {user.last_name if user.last_name else ''}".strip()
    
    keyboard = [
        [
            InlineKeyboardButton("🛠 Menu", callback_data="menu"),
            InlineKeyboardButton("💻 Apps", callback_data="apps"),
            InlineKeyboardButton("🌐 Website", url="https://srr0.blogspot.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        f"{user_name}\nWelcome to Sajedur0!",
        reply_markup=reply_markup
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📥 TG ID Check", callback_data="TG_ID"),
            InlineKeyboardButton("🎂 Age Calculator", callback_data="/pin")
        ],
        [
            InlineKeyboardButton("🔳 QR Code Make", callback_data="/test"),
            InlineKeyboardButton("🚧 Coming Soon", callback_data="/Comming_Soon")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "⤵️ Choose below:",
        reply_markup=reply_markup
    )

async def apps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [InlineKeyboardButton("1 - Fonts", callback_data="getfile_2")],
        [InlineKeyboardButton("All Fonts", callback_data="getfile_3")],
        [InlineKeyboardButton("Arabic Fonts", callback_data="getfile_4")],
        [InlineKeyboardButton("Bangla Fonts", callback_data="getfile_5")],
        [InlineKeyboardButton("Bijoy Stylish Fonts", callback_data="getfile_6")],
        [InlineKeyboardButton("Adobe Patch", callback_data="getfile_7")],
        [InlineKeyboardButton("Creative Cloud Uninstaller x64", callback_data="getfile_8")],
        [InlineKeyboardButton("Creative Cloud Uninstaller x86", callback_data="getfile_9")],
        [InlineKeyboardButton("Lan Driver Full Package", callback_data="getfile_10")],
        [InlineKeyboardButton("Tende Driver", callback_data="getfile_11")],
        [InlineKeyboardButton("TP-LINK Driver", callback_data="getfile_12")],
        [InlineKeyboardButton("Office 365 ProPlus Online Installer", callback_data="getfile_13")],
        [InlineKeyboardButton("WinRAR v6.11", callback_data="getfile_14")],
        [InlineKeyboardButton("Printer Fix Error", callback_data="getfile_15")],
        [InlineKeyboardButton("Office Uninstaller", callback_data="getfile_16")],
        [InlineKeyboardButton("Google Drive Uninstaller", callback_data="getfile_17")],
        [InlineKeyboardButton("Adobe Patch", callback_data="getfile_18")],
        [InlineKeyboardButton("Windows 7 Activator", callback_data="getfile_19")],
        [InlineKeyboardButton("🔙 Back", callback_data="start")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await update.message.reply_text(
        "📂 **Select a file:**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    data = query.data
    
    if data == "start":
        await start_callback(update, context)
    elif data == "menu":
        await menu_callback(update, context)
    elif data == "apps":
        await apps_callback(update, context)
    elif data.startswith("getfile_"):
        file_number = data.split("_")[1]
        await send_file(update, context, file_number)
    elif data in ["TG_ID", "/pin", "/test", "/Comming_Soon"]:
        await query.edit_message_text(f"Command received: {data}\nThis feature is under development.")

async def start_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    user_name = f"Hey {user.first_name} {user.last_name if user.last_name else ''}".strip()
    
    keyboard = [
        [
            InlineKeyboardButton("🛠 Menu", callback_data="menu"),
            InlineKeyboardButton("💻 Apps", callback_data="apps"),
            InlineKeyboardButton("🌐 Website", url="https://srr0.blogspot.com")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        f"{user_name}\nWelcome to Sajedur0!",
        reply_markup=reply_markup
    )

async def menu_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    keyboard = [
        [
            InlineKeyboardButton("📥 TG ID Check", callback_data="TG_ID"),
            InlineKeyboardButton("🎂 Age Calculator", callback_data="/pin")
        ],
        [
            InlineKeyboardButton("🔳 QR Code Make", callback_data="/test"),
            InlineKeyboardButton("🚧 Coming Soon", callback_data="/Comming_Soon")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await query.edit_message_text(
        "⤵️ Choose below:",
        reply_markup=reply_markup
    )

async def apps_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    
    buttons = [
        [InlineKeyboardButton("1 - Fonts", callback_data="getfile_2")],
        [InlineKeyboardButton("All Fonts", callback_data="getfile_3")],
        [InlineKeyboardButton("Arabic Fonts", callback_data="getfile_4")],
        [InlineKeyboardButton("Bangla Fonts", callback_data="getfile_5")],
        [InlineKeyboardButton("Bijoy Stylish Fonts", callback_data="getfile_6")],
        [InlineKeyboardButton("Adobe Patch", callback_data="getfile_7")],
        [InlineKeyboardButton("Creative Cloud Uninstaller x64", callback_data="getfile_8")],
        [InlineKeyboardButton("Creative Cloud Uninstaller x86", callback_data="getfile_9")],
        [InlineKeyboardButton("Lan Driver Full Package", callback_data="getfile_10")],
        [InlineKeyboardButton("Tende Driver", callback_data="getfile_11")],
        [InlineKeyboardButton("TP-LINK Driver", callback_data="getfile_12")],
        [InlineKeyboardButton("Office 365 ProPlus Online Installer", callback_data="getfile_13")],
        [InlineKeyboardButton("WinRAR v6.11", callback_data="getfile_14")],
        [InlineKeyboardButton("Printer Fix Error", callback_data="getfile_15")],
        [InlineKeyboardButton("Office Uninstaller", callback_data="getfile_16")],
        [InlineKeyboardButton("Google Drive Uninstaller", callback_data="getfile_17")],
        [InlineKeyboardButton("Adobe Patch", callback_data="getfile_18")],
        [InlineKeyboardButton("Windows 7 Activator", callback_data="getfile_19")],
        [InlineKeyboardButton("🔙 Back", callback_data="start")]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await query.edit_message_text(
        "📂 **Select a file:**",
        reply_markup=reply_markup,
        parse_mode='Markdown'
    )

async def send_file(update: Update, context: ContextTypes.DEFAULT_TYPE, file_number: str):
    query = update.callback_query
    file_url = f"https://t.me/Sajedur0Server/{file_number}?single"
    
    await query.message.reply_document(
        document=file_url,
        caption=f"📂 **File {file_number}**\nStay with @Sajedur0",
        parse_mode='Markdown'
    )

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("menu", menu))
    application.add_handler(CommandHandler("apps", apps))
    application.add_handler(CallbackQueryHandler(button_handler))
    
    application.run_polling()

if __name__ == '__main__':
    main()