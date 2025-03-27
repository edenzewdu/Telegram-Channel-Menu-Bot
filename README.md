Telegram Channel Menu Bot
This project creates a folder-style menu inside a Telegram channel using a bot. The bot posts a structured menu with clickable buttons, allowing users to navigate different categories.
________________________________________
Features
✅ Posts a menu with categories inside a Telegram channel
✅ Users can click buttons to explore subcategories
✅ Direct links to posts inside the channel
✅ Uses inline buttons to create a structured menu
________________________________________
Installation
1️⃣ Install Required Packages
Ensure you have Python installed, then install pyTelegramBotAPI:
pip install pyTelegramBotAPI
2️⃣ Create a Telegram Bot
1.	Open Telegram and search for @BotFather.
2.	Send /newbot and follow the instructions.
3.	Copy the bot token provided.
________________________________________
Setup & Configuration
3️⃣ Configure the Script
Edit telegram_channel_menu.py and replace:
•	BOT_TOKEN = "YOUR_BOT_TOKEN" → Insert your bot token
•	CHANNEL_USERNAME = "@YourChannelUsername" → Replace with your channel username
4️⃣ Add Bot to Your Channel
1.	Open your Telegram channel.
2.	Go to Manage Channel → Administrators.
3.	Add your bot as an admin.
4.	Give it post permissions.
________________________________________
Running the Bot
Run the script to post the menu in your channel:
python telegram_channel_menu.py
Once posted, pin the message in your channel for easy access.
________________________________________
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
________________________________________
Notes
•	Ensure your bot is an admin in the channel.
•	Pin the menu message for easy navigation.
•	Modify the categories as needed inside the categories dictionary.
🚀 Enjoy your Telegram Channel Menu Bot!

