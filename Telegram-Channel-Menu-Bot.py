bot = telebot.TeleBot(BOT_TOKEN)
import telebot
import schedule
import time
import datetime
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your bot token
BOT_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_ID = "@YourChannelUsername"  # Replace with your channel username
GROUP_IDS = [-100XXXXXXXX, -100XXXXXXXX]  # Replace with actual group IDs

bot = telebot.TeleBot(BOT_TOKEN)

# Function to get yesterday's timestamp
def get_yesterday():
    return datetime.datetime.now() - datetime.timedelta(days=1)

# Fetch messages from the last 24 hours using get_chat_history()
def fetch_daily_messages():
    yesterday = get_yesterday().timestamp()
    new_books = []

    for group_id in GROUP_IDS:
        try:
            chat_history = bot.get_chat_history(group_id, limit=50)

            for message in chat_history.messages:
                if message.date >= yesterday and message.text:
                    book_link = f"https://t.me/{message.chat.username}/{message.message_id}"
                    new_books.append(f"🔹 {message.text}\n📌 [Read More]({book_link})")

        except Exception as e:
            print(f"⚠️ Error fetching messages from {group_id}: {e}")

    return new_books

# Post daily summary of books
def post_daily_summary():
    new_books = fetch_daily_messages()

    if new_books:
        summary_text = "**📚 New Books of the Day:**\n\n" + "\n\n".join(new_books)
        bot.send_message(CHANNEL_ID, summary_text, parse_mode="Markdown", disable_web_page_preview=True)
    else:
        bot.send_message(CHANNEL_ID, "📭 No new books added today.")

# Category dictionary
categories = {
    "📚 Kindergarten": "https://t.me/educationalBooks1/2",
    "📘 Grade 1": "https://t.me/educationalBooks1/4",
    "📗 Grade 2": "https://t.me/educationalBooks1/6",
    "📙 Grade 3": "https://t.me/educationalBooks1/8",
    "📕 Grade 4": "https://t.me/educationalBooks1/10",
    "📖 Grade 5": "https://t.me/educationalBooks1/12",
    "📔 Grade 6": "https://t.me/educationalBooks1/14",
    "📒 Grade 7": "https://t.me/educationalBooks1/16",
    "📓 Grade 8": "https://t.me/educationalBooks1/18",
    "📔 Grade 9": "https://t.me/educationalBooks1/20",
    "📕 Grade 10": "https://t.me/educationalBooks1/22",
    "📖 Grade 11 - Social Science": "https://t.me/educationalBooks1/24",
    "📖 Grade 11 - Natural Science": "https://t.me/educationalBooks1/26",
    "📖 Grade 12 - Social Science": "https://t.me/educationalBooks1/44",
    "📖 Grade 12 - Natural Science": "https://t.me/educationalBooks1/46",
    "📖 Spiritual Books": "https://t.me/MKCpagesofwisdom/14",
    "📚 Literature": "https://t.me/MKCpagesofwisdom/3",
    "🧠 Psychology Books": "https://t.me/MKCpagesofwisdom/16",
    "🌍 General Knowledge": "https://t.me/Other_Purpose_Books/18",
    "📰 News Papers": "https://t.me/MKCpagesofwisdom/20",
    "📖 Novels": "https://t.me/MKCpagesofwisdom/22",
    "📜 History Books": "https://t.me/MKCpagesofwisdom/24",
}

# /start command that posts category links to the channel
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = InlineKeyboardMarkup()
    for category, link in categories.items():
        button = InlineKeyboardButton(category, url=link)
        markup.add(button)

    bot.send_message(
        CHANNEL_ID,
        "📚 **Welcome! Choose a Book Category Below:**",
        reply_markup=markup,
        parse_mode="Markdown"
    )

# /categories command that sends the category list to the user
@bot.message_handler(commands=['categories'])
def send_category_links(message):
    markup = InlineKeyboardMarkup()
    for category, link in categories.items():
        button = InlineKeyboardButton(category, url=link)
        markup.add(button)

    bot.send_message(message.chat.id, "📂 **Choose a Category**:", reply_markup=markup, parse_mode="Markdown")

# Welcome new members
@bot.message_handler(content_types=['new_chat_members'])
def welcome_new_member(message):
    bot.send_message(
        message.chat.id,
        "👋 Welcome to **Mizan MKC Digital Library**! 📚\n"
        "Use /categories to explore books by category. Happy reading! 😊",
        parse_mode="Markdown"
    )

# Run bot and schedule tasks
if __name__ == "__main__":
    while True:
        schedule.run_pending()
        time.sleep(60)  # Check every 60 seconds for scheduled tasks
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"Polling error: {e}")
            time.sleep(15)

