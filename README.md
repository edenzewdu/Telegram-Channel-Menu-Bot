Telegram Channel Menu Bot

This project creates a folder-style menu inside a Telegram channel using a bot. The bot posts a structured menu with clickable buttons, allowing users to navigate different categories.

Features

✅ Posts a menu with categories inside a Telegram channel✅ Users can click buttons to explore subcategories✅ Direct links to posts inside the channel✅ Uses inline buttons to create a structured menu

Installation

1️⃣ Install Required Packages

Ensure you have Python installed, then install pyTelegramBotAPI:

pip install pyTelegramBotAPI

2️⃣ Create a Telegram Bot

Open Telegram and search for @BotFather.

Send /newbot and follow the instructions.

Copy the bot token provided.

Setup & Configuration

3️⃣ Configure the Script

Edit telegram_channel_menu.py and replace:

BOT_TOKEN = "YOUR_BOT_TOKEN" → Insert your bot token

CHANNEL_USERNAME = "@YourChannelUsername" → Replace with your channel username

4️⃣ Add Bot to Your Channel

Open your Telegram channel.

Go to Manage Channel → Administrators.

Add your bot as an admin.

Give it post permissions.

Running the Bot

Run the script to post the menu in your channel:

python telegram_channel_menu.py

Once posted, pin the message in your channel for easy access.

Folder Structure

📂 Main Menu
 ├── 📘 Kindergarten
 ├── 📗 Grade 1
 ├── 📙 Grade 2
 ├── 📕 Grade 3
 ├── 📖 Grade 11
 │    ├── 📚 Social Science
 │    ├── 🔬 Natural Science
 ├── 📖 Grade 12
 │    ├── 📚 Social Science
 │    ├── 🔬 Natural Science
 ├── 📜 History Books
 ├── 📰 News Papers
 └── 📚 Literature

Notes

Ensure your bot is an admin in the channel.

Pin the menu message for easy navigation.

Modify the categories as needed inside the categories dictionary.

🚀 Enjoy your Telegram Channel Menu Bot!
