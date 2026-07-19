import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Products", callback_data="products")],
        [InlineKeyboardButton("💰 Prices", callback_data="prices")],
        [InlineKeyboardButton("💳 Payment", callback_data="payment")],
        [InlineKeyboardButton("📞 Contact", callback_data="contact")],
    ]

    await update.message.reply_text(
        "💎 EVA AI MARKET\n\n"
        "Welcome!\n"
        "Choose an option below.",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "products":
        text = """☁️ AWS CLOUD

☁️ AWS 128V • 256V • 512V

✅ Amazon Bedrock Claude AI Opus
✅ GPT Plus + Claude Access
✅ Gemini Ultra Support

🌍 International
⚡ Instant Delivery
"""

    elif query.data == "prices":
        text = """💰 PRICE LIST

☁️ AWS
• 128V — $100
• 256V — $180
• 512V — $250

🤖 AI
• Claude Pro — 15 USDT
• Claude Max 5 — 35 USDT
• Claude Max 20 — 80 USDT

👑 GPT
• GPT Plus — 130 USDT
• GPT Pro — 140 USDT
"""

    elif query.data == "payment":
        text = """💳 EVA AI MARKET
━━━━━━━━━━━━━━━━━━━━

💰 PAYMENT METHODS

🟢 USDT (TRC20)

TJCFS6hDKsEnquGuvw43krk141QLvHnGbG

━━━━━━━━━━━━━━━━━━━━

🟡 USDT (BEP20)

0x644ed89caecc120d3a3180e9f20a90d970cfa3e8

━━━━━━━━━━━━━━━━━━━━

📩 AFTER PAYMENT

✔ Send Payment Screenshot
✔ Send TXID / Transaction Hash
✔ Mention Your Order

━━━━━━━━━━━━━━━━━━━━

👤 CONTACT ADMIN

@eva007_8

━━━━━━━━━━━━━━━━━━━━

📢 OFFICIAL CHANNELS

EVA AI MARKET
https://t.me/evacloudhub247

AWS CLOUD MARKET
https://t.me/AWSXCLOUDEBUYSELL

━━━━━━━━━━━━━━━━━━━━

✅ Instant Delivery
✅ Fast Support
✅ Trusted Seller
✅ Worldwide Service

Thank you for choosing
💎 EVA AI MARKET
"""

    elif query.data == "contact":
        text = """📞 Contact Us

👤 Admin: @eva007_8

📢 Official Channels:
• EVA AI MARKET → https://t.me/evacloudhub247
• AWS CLOUD MARKET → https://t.me/AWSXCLOUDEBUYSELL

💬 Any query? Feel free to message the admin."""

    else:
        text = "Unknown option."

    # Edit the original message
    await query.edit_message_text(text, parse_mode="HTML")


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set!")

    application = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(buttons))

    # Run the bot
    print("🤖 EVA AI Market Bot is running...")
    application.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
