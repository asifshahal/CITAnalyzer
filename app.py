import os
import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo,
)
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters,
)

# ---------------- CONFIG ----------------
BOT_TOKEN = os.getenv("BOT_TOKEN")
MINI_APP_URL = "https://yourdomain.com"  # <-- CHANGE THIS
# ----------------------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                text="🚀 Open Mini App",
                web_app=WebAppInfo(url=MINI_APP_URL),
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Welcome 👋\n\n"
        "This bot works together with our Telegram Mini App.\n\n"
        "Tap the button below to open the app and start your analysis.",
        reply_markup=reply_markup,
    )

# Receive data from Mini App
async def web_app_data_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data

    await update.message.reply_text(
        "📊 Analysis Result:\n\n"
        f"{data}\n\n"
        "⚠️ This analysis is informational only and not financial advice."
    )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN environment variable not set")

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_app_data_handler)
    )

    app.run_polling()

if __name__ == "__main__":
    main()
