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

MINI_APP_URL = "t.me/Citchartanalyzer_bot/citanalyzer"
SUPPORT_URL = "https://t.me/CITsupport"
COMMUNITY_URL = "https://t.me/cryptoinfo_tamil"

START_TEXT = (
    "🚀 *Welcome to CIT Analyzer*\n\n"
    "Upload *any chart image* — Crypto, Stocks, Gold, or Forex — and receive "
    "*instant, in-depth technical analysis* powered by *CIT Analyzer*.\n\n"
    "🔍 *What You Get*\n"
    "• Trend direction & market structure\n"
    "• Key support and resistance levels\n"
    "• Indicator insights (RSI, MACD, EMAs, patterns)\n"
    "• Momentum & volatility analysis\n"
    "• Actionable bias (bullish / bearish / neutral)\n\n"
    "📊 *Supported Markets*\n"
    "• Cryptocurrencies\n"
    "• Stocks & Indices\n"
    "• Gold & Commodities\n"
    "• Forex pairs\n\n"
    "📤 *How It Works*\n"
    "1. Upload a clear chart screenshot\n"
    "2. Our engine analyzes price action & indicators\n"
    "3. Receive a detailed technical breakdown in seconds\n\n"
    "⚠️ _For educational and informational purposes only. Not financial advice._\n\n"
    "📈 *Trade smarter with CIT Analyzer*\n"
    "Send a chart image to begin."
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
