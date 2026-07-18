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
    elif data == "prices":
        text = """💎 EVA AI MARKET
━━━━━━━━━━━━━━━━━━━━

🤖 AI ACCOUNTS

• Claude Pro ─ 15 USDT │ 15 Days
• Claude Max 5 ─ 35 USDT
• Claude Max 20 ─ 80 USDT
• Claude Max 20 (365 Days) ─ 150 USDT

👑 GPT

• GPT Pro ─ 140 USDT │ 1 Year Warranty
• GPT Plus (GPT-4o) ─ 130 USDT

✨ AI TOOLS

• Gemini Ultra / Veo 3
  ├ Warranty ─ $15
  └ No Warranty ─ $7

• Super Grok ─ $100
  └ 1 Year Warranty

• Kling Pro ─ $15
  ├ 4500 Credits
  └ 5 Days Warranty

• CapCut Pro
  ├ 1 Month ─ $8
  ├ 3 Months ─ $25
  ├ 6 Months ─ $45
  └ 12 Months ─ $80

━━━━━━━━━━━━━━━━━━━━

☁️ AWS CLOUD

• 8 vCPU ─ $30
• 16 vCPU ─ $50
• 64 vCPU ─ $80
• 128 vCPU ─ $100
• 256 vCPU ─ $180
• 512 vCPU ─ $250

💳 AWS CREDITS

• $1,000 Credits ─ $120
• $5,000 Credits ─ $500
• $10,000 Credits ─ $700

☁️ GCP

• GCP $300
• GCP $5,000
• GCP $25,000
• GCP $50,000
• GCP $100,000

📩 Contact: @eva007_8
🔥 IN STOCK • INSTANT DELIVERY
"""

    elif data == "payment":
        text = """💳 PAYMENT METHODS

USDT (TRC20)
TJCFS6hDKsEnquGuvw43krk141QLvHnGbG

USDT (BEP20)
0x644ed89caecc120d3a3180e9f20a90d970cfa3e8

After payment, send the transaction ID to the     elif data == "order":
        text = """📦 ORDER PROCESS

1. Select your product
2. Contact the admin
3. Complete payment
4. Receive your service

👨‍💻 Admin: @eva007_8
"""

    elif data == "contact":
        text = """👨‍💻 CONTACT ADMIN

Telegram:
@eva007_8
"""

    elif data == "channel":
        text = """📢 OFFICIAL CHANNEL

https://t.me/evacloudhub247
"""

    elif data == "reviews":
        text = """⭐ CUSTOMER REVIEWS

https://t.me/AWSXCLOUDEBUYSELL
"""

    else:
        text = "Please choose an option."

    await query.edit_message_text(text=text)


def main():
    if not BOT_TOKEN:
        raise ValueError("BOT_TOKEN environment variable is not set.")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
