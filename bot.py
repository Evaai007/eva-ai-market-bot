import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛒 Product List", callback_data="products")],
        [InlineKeyboardButton("💸 Price List", callback_data="prices")],
        [InlineKeyboardButton("💳 Payment", callback_data="payment")],
        [InlineKeyboardButton("📦 Order Now", callback_data="order")],
        [InlineKeyboardButton("👨‍💻 Contact Admin", callback_data="contact")],
        [InlineKeyboardButton("📢 Channel", callback_data="channel")],
        [InlineKeyboardButton("⭐ Reviews", callback_data="reviews")],
    ]

    await update.message.reply_text(
        "💎 EVA AI MARKET\n\n"
        "🚀 Premium AI Accounts & Cloud Services\n\n"
        "Choose an option below 👇",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


async def button(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "products":
        text = """🛒 PRODUCT LIST

🤖 AI ACCOUNTS
• Claude Pro
• Claude Max 5
• Claude Max 20

👑 GPT
• GPT Pro
• GPT Plus

✨ AI TOOLS
• Gemini Ultra
• Super Grok
• Kling Pro
• CapCut Pro

☁️ CLOUD
• AWS
• GCP
• Oracle
• Azure
"""

    elif data == "prices":
        text = "💸 Price List is loading..."

    elif data == "payment":
        text = """💳 PAYMENT METHODS

USDT TRC20:
TJCFS6hDKsEnquGuvw43krk141QLvHnGbG

USDT BEP20:
0x644ed89caecc120d3a3180e9f20a90d970cfa3e8

After payment contact admin.
"""

    elif data == "order":
        text = """📦 ORDER PROCESS

1. Select product
2. Contact Admin
3. Complete payment
4. Receive service

👨‍💻 @eva007_8
"""

    elif data == "contact":
        text = "👨‍💻 Contact Admin\n\nTelegram: @eva007_8"

    elif data == "channel":
        text = "📢 Official Channel\n\nhttps://t.me/evacloudhub247"

    elif data == "reviews":
        text = "⭐ Customer Reviews\n\nhttps://t.me/AWSXCLOUDEBUYSELL"

    else:
        text = "Please choose an option."

    await query.edit_message_text(text=text)


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    app.run_polling()


if __name__ == "__main__":
    main()
