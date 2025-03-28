# Telegram Bot for Educational Books Navigation

## Overview
This Telegram bot helps users navigate different categories of educational books and related topics. Users can select categories and subcategories, and the bot provides links to relevant Telegram groups and subtopics.

## Features
- 📂 **Category Selection**: Users can browse different book categories.
- 📁 **Subcategory Navigation**: Users can access subtopics within categories.
- 🔗 **Direct Links**: Automatically generates and provides links to relevant Telegram groups and subtopics.
- 🔄 **Interactive Menu**: Uses inline buttons for a smooth navigation experience.

## Requirements
- Python 3.x
- `pyTelegramBotAPI` library
- A valid Telegram Bot Token

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/telegram-bot.git
   cd telegram-bot
   ```
2. Install dependencies:
   ```sh
   pip install pyTelegramBotAPI
   ```
3. Set up your Telegram Bot Token in the script:
   ```python
   BOT_TOKEN = "your_bot_token_here"
   ```

## Usage
1. Start the bot using:
   ```sh
   python bot.py
   ```
2. Send `/start` or `/menu` in the chat to display the category menu.
3. Click on a category to view available subtopics.
4. Click on a subtopic to navigate directly to the Telegram group or topic.

## Bot Commands
- `/start` - Start the bot and display the menu.
- `/menu` - Show the category menu again.

## Structure
- **`bot.py`** - Main script for running the bot.
- **`README.md`** - Documentation file.

## Contributing
Feel free to submit issues and pull requests to enhance the bot's functionality.

## License
This project is licensed under the MIT License.

