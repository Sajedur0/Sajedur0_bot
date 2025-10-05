import logging
import qrcode
import io
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes, MessageHandler, filters

# বটের টোকেন
BOT_TOKEN = "7841530700:AAETQrppsCGhL_IQM_qCvWPPs8U9yJWMQlg"

# লগিং কনফিগারেশন
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# QR কোড জেনারেট করার ফাংশন
def generate_qr_code(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    
    # ইমেজকে বাইট স্ট্রিমে কনভার্ট করুন
    bio = io.BytesIO()
    img.save(bio, 'PNG')
    bio.seek(0)
    
    return bio

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
            InlineKeyboardButton("🔳 QR Code Make", callback_data="qr_code"),
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

async def qr_code_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    # ইউজারকে টেক্সট ইনপুটের জন্য বলুন
    await query.edit_message_text(
        "🔳 **QR Code Generator**\n\n"
        "Please send me the text/URL you want to convert to QR code:"
    )
    
    # কনটেক্সটে স্টেট সেট করুন
    context.user_data['waiting_for_qr_text'] = True

async def handle_text_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # চেক করুন যদি ইউজার QR কোড টেক্সট দিতে চায়
    if context.user_data.get('waiting_for_qr_text'):
        text = update.message.text
        
        # QR কোড জেনারেট করুন
        try:
            qr_image = generate_qr_code(text)
            
            # QR কোড ইমেজ পাঠান
            await update.message.reply_photo(
                photo=qr_image,
                caption=f"✅ **QR Code Generated Successfully!**\n\n📝 **Text:** {text}\n\nStay with @Sajedur0",
                parse_mode='Markdown'
            )
            
            # মেনু বাটন সহ মেসেজ পাঠান
            keyboard = [
                [
                    InlineKeyboardButton("🛠 Main Menu", callback_data="start"),
                    InlineKeyboardButton("🔳 Make Another QR", callback_data="qr_code")
                ]
            ]
            reply_markup = InlineKeyboardMarkup(keyboard)
            
            await update.message.reply_text(
                "⤵️ What would you like to do next?",
                reply_markup=reply_markup
            )
            
        except Exception as e:
            await update.message.reply_text(
                f"❌ Error generating QR code: {str(e)}\nPlease try again."
            )
        
        # স্টেট রিসেট করুন
        context.user_data['waiting_for_qr_text'] = False
        return

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
    elif data == "qr_code":
        await qr_code_handler(update, context)
    elif data.startswith("getfile_"):
        file_number = data.split("_")[1]
        await send_file(update, context, file_number)
    elif data in ["TG_ID", "/pin", "/Comming_Soon"]:
        await query.edit_message_text(f"Command received: {data}\nThis feature is under development.")
    elif data == "/test":
        await qr_code_handler(update, context)

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
            InlineKeyboardButton("🔳 QR Code Make", callback_data="qr_code"),
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
    
    # টেক্সট মেসেজ হ্যান্ডলার যোগ করুন (QR কোড জেনারেশনের জন্য)
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text_message))
    
    application.run_polling()

if __name__ == '__main__':
    main()