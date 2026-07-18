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
  ✔ Full Warranty

━━━━━━━━━━━━━━━━━━━━
"""☁️ AWS CLOUD

Bedrock Claude AI Opus

✅ Working Normally
✅ Opus 4.6
✅ Opus 4.7
✅ Opus 4.8

Standard vCPU

• 8 vCPU ─ $30
• 16 vCPU ─ $50
• 64 vCPU ─ $80
• 128 vCPU ─ $100
• 256 vCPU ─ $180
• 512 vCPU ─ $250

━━━━━━━━━━━━━━━━━━━━

🚀 PREMIUM AWS INVENTORY

• 64 vCPU │ 10K RPM ─ $140
• 96 vCPU │ 10K RPM ─ $180
• 128 vCPU │ 10K RPM ─ $300
• 256 vCPU │ 10K RPM ─ $500
• 512 vCPU │ 10K RPM │ USA IP ─ $250
• 10K RPM │ Random IP ─ $80
• 1280 vCPU │ 10K RPM │ Old Account ─ $1100
• 384 vCPU │ Old Account ─ $2500

━━━━━━━━━━━━━━━━━━━━

💳 AWS CREDITS

• $300 AWS
• $1,000 Credits ─ $120
• $5,000 Credits ─ $500
• $10,000 Credits ─ $700

━━━━━━━━━━━━━━━━━━━━

☁️ GCP

Available:

• GCP $300
• GCP $5,000
• GCP $25,000
• GCP $50,000
• GCP $100,000

✅ Tier 3 AI Studio Billing
✅ Gemini Supported
✅ Cloud Run Ready

━━━━━━━━━━━━━━━━━━━━

☁️ CLOUD SERVICES

• Oracle $300 PAYG
• Oracle London ─ $25
• Oracle Stockholm ─ $25

• Azure PAYG ─ $20
• Azure Plans ─ $8 / $10 / $12

• DigitalOcean $200 (1 Year)
• Vultr $300 Credit ─ $12
• Linode $1000 Old Account
• OVH Free Trial ─ $12
• OVH 34 vCPU ─ $15
• UpCloud ─ $12 / $18
• Kamatera ─ $12

━━━━━━━━━━━━━━━━━━━━

💼 BUSINESS

✔ Long-Term Orders Accepted
✔ Bulk Orders Available
✔ Fast Delivery
✔ Professional Support
✔ Worldwide Service

📩 Contact: @eva007_8

🔥 IN STOCK • INSTANT DELIVERY


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
