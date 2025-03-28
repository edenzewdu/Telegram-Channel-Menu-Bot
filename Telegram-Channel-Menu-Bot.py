import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = -100XXXXXXXX
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

# Group links for each category
group_links = {
    "📚 Kindergarten": "https://t.me/Kindergarten_Group",
    "📘 Grade 1": "https://t.me/Grade1_Group",
    "📗 Grade 2": "https://t.me/Grade2_Group",
    "📙 Grade 3": "https://t.me/Grade3_Group",
    "📕 Grade 4": "https://t.me/Grade4_Group",
    "📖 Grade 5": "https://t.me/Grade5_Group",
    "📔 Grade 6": "https://t.me/Grade6_Group",
    "📒 Grade 7": "https://t.me/Grade7_Group",
    "📓 Grade 8": "https://t.me/Grade8_Group",
    "📔 Grade 9": "https://t.me/Grade9_Group",
    "📕 Grade 10": "https://t.me/Grade10_Group",
    "📖 Grade 11": "https://t.me/Grade11_Group",
    "📖 Grade 12": "https://t.me/Grade12_Group",
    "📖 Spiritual Books": "https://t.me/SpiritualBooks_Group",
    "📚 Literature": "https://t.me/Literature_Group",
    "🧠 Psychology Books": "https://t.me/Psychology_Group",
    "🌍 General Knowledge": "https://t.me/GeneralKnowledge_Group",
    "📰 News Papers": "https://t.me/NewsPapers_Group",
    "📖 Novels": "https://t.me/Novels_Group",
    "📜 History Books": "https://t.me/HistoryBooks_Group"
}

# Function to generate inline keyboard for main menu
def generate_menu():
    markup = InlineKeyboardMarkup()
    
    for category, subcategories in categories.items():
        if subcategories:
            markup.add(InlineKeyboardButton(f"📂 {category}", callback_data=category))
        else:
            group_url = group_links.get(category, f"https://t.me/{CHANNEL_USERNAME}")  # Fallback to channel
            markup.add(InlineKeyboardButton(f"📁 {category}", url=group_url))

    return markup

@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    """Send the menu to the Telegram Channel."""
    bot.send_message(CHANNEL_ID, "📂 **Choose a Category:**", reply_markup=generate_menu(), parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data in categories)
def show_subcategories(call):
    """Display subcategories when a category is clicked."""
    subcategories = categories[call.data]
    markup = InlineKeyboardMarkup()

    if subcategories:
        for sub in subcategories:
            group_url = group_links.get(call.data, f"https://t.me/{CHANNEL_USERNAME}")  # Fallback to channel
            markup.add(InlineKeyboardButton(sub, url=group_url))
        bot.send_message(call.message.chat.id, f"📂 **{call.data} contains:**", reply_markup=markup, parse_mode="Markdown")
    else:
        bot.answer_callback_query(call.id, "This category doesn't have subcategories.")

# Run the bot
bot.polling()
