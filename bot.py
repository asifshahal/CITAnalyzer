import os
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    WebAppInfo
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

MINI_APP_URL = "https://t.me/YourBot/yourMiniApp"
SUPPORT_URL = "https://t.me/YourSupportUsername"
COMMUNITY_URL = "https://t.me/YourCommunityChannel"

START_TEXT = (
    "🚀 *Welcome to GasPe, CIT!*\n\n"
    "Your trusted cryptocurrency trading platform offering:\n\n"
    "💰 *Buy Crypto with INR*\n"
    "• BNB, ETH, SOL and more\n"
    "• Transparent package-based pricing\n"
    "• Instant transactions\n\n"
    "🔄 *Instant Sell Feature*\n"
    "• Quick crypto-to-INR conversion\n"
    "• Competitive rates\n"
    "• Fast processing\n\n"
    "⚡ *Why Choose GasPe?*\n"
    "• Secure & Regulated\n"
    "• 24/7 Customer Support\n"
    "• Best exchange rates in India\n"
    "• Easy-to-use interface\n\n"
    "📲 *Ready to start trading?*\n"
    "Click the button below to open our secure trading platform!\n\n"
    "_Trade smart, trade with GasPe ✨_"
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🚀 Open GasPe Trading App",
                web_app=WebAppInfo(url=MINI_APP_URL)
            )
        ],
        [
            InlineKeyboardButton("📞 Support", url=SUPPORT_URL),
            InlineKeyboardButton("📢 Join Community", url=COMMUNITY_URL)
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        START_TEXT,
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_webhook(
        listen="0.0.0.0",
        port=int(os.getenv("PORT", 8080)),
        webhook_url=os.getenv("WEBHOOK_URL")
    )

if __name__ == "__main__":
    main()
