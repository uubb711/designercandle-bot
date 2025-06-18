
import os
import telebot

# Получаем токен из переменной окружения
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

# Company Info
company_info = (
    "Designer Candle was founded in 2025 by Usmanova A.U. "
    "We craft handmade eco-friendly candles with unique designs. "
    "Perfect for gifts and cozy decor."
)

# Products and Services
products_services = (
    "🕯️ Soy Candles: Natural wax, various scents.\n"
    "✨ Decorative Holders: Handmade holders for candles.\n"
    "🎁 Gift Sets: Beautifully packed candle sets for special occasions."
)


# FAQ
faq = (
    "❓ What candles do you offer? We make soy candles, custom designs, and gift sets."

    "🛒 How to order? Just send us a message with your preferred product."

    "🚚 Do you deliver? Yes! We offer local delivery and shipping."
)

# Welcome Message
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! I'm the Designer Candle bot. How can I assist you today?\nUse /history for our story, /products for candles and gift sets, /faq for common questions.")

# Company History
@bot.message_handler(commands=['history'])
def send_history(message):
    bot.reply_to(message, company_info)

# Product and Service List
@bot.message_handler(commands=['products'])
def send_products(message):
    bot.reply_to(message, products_services)

# Frequently Asked Questions
@bot.message_handler(commands=['faq'])
def send_faq(message):
    bot.reply_to(message, faq)

# Start the bot
print("✅ Designer Candle Bot is running...")
bot.infinity_polling()
