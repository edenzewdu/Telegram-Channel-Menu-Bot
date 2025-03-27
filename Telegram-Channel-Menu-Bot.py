import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@YourChannelUsername"  # Replace with your channel username

bot = telebot.TeleBot(BOT_TOKEN)

# Define categories and subcategories
categories = {
    "📚 Kindergarten": None,
    "📘 Grade 1": None,
    "📗 Grade 2": None,
    "📙 Grade 3": None,
    "📕 Grade 4": None,
    "📖 Grade 5": None,
    "📔 Grade 6": None,
    "📒 Grade 7": None,
    "📓 Grade 8": None,
    "📔 Grade 9": None,
    "📕 Grade 10": None,
    "📖 Grade 11": ["📚 Social Science", "🔬 Natural Science"],
    "📖 Grade 12": ["📚 Social Science", "🔬 Natural Science"],
    "📖 Spiritual Books": None,
    "📚 Literature": None,
    "🧠 Psychology Books": None,
    "🌍 General Knowledge": None,
    "📰 News Papers": None,
    "📖 Novels": None,
    "📜 History Books": None
}

# Function to generate inline keyboard for main menu
def generate_menu():
    markup = InlineKeyboardMarkup()
    
    for category, subcategories in categories.items():
        if subcategories:
            markup.add(InlineKeyboardButton(f"📂 {category}", callback_data=category))
        else:
            markup.add(InlineKeyboardButton(f"📁 {category}", url=f"https://t.me/{CHANNEL_USERNAME}"))

    return markup

@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    bot.send_message(CHANNEL_USERNAME, "📂 **Choose a Category:**", reply_markup=generate_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in categories)
def show_subcategories(call):
    subcategories = categories[call.data]
    markup = InlineKeyboardMarkup()
    
    for sub in subcategories:
        markup.add(InlineKeyboardButton(sub, url=f"https://t.me/{CHANNEL_USERNAME}"))
    
    bot.send_message(call.message.chat.id, f"📂 **{call.data} contains:**", reply_markup=markup, parse_mode="Markdown")

# Run the bot
bot.polling()
