# 📨 Telegram Bot for forum.wayzer.ru Integration

This Telegram bot allows users to send messages to [forum.wayzer.ru](https://forum.wayzer.ru) through `flarum_remember`. Users can set their `flarum_remember` token by clicking the **Change flarum** button in the bot. If no token is provided, it defaults to `NULL`. The bot forwards messages to a specified discussion thread on the forum based on user input.

---

## 🚀 Features

- **Flarum Integration:** Users can send messages to the Wayzer Forum.
- **Token Management:** Users can set or update their `flarum_remember` token in the bot.
- **Easy Messaging:** Forward messages directly to the forum by specifying the discussion ID and message.
- **Database:** Uses `aiosqlite` to store and manage user tokens.

---

## 🛠️ File Structure

```
├── main.py                 # Entry point of the bot, contains the bot token
├── modules/                # Contains all core modules
│   ├── libraries/
│   │   ├── utils.py        # Holds states, keyboards, constants
│   │   ├── dbms.py         # Functions for database interaction
│   │   ├── sender.py       # Class to send messages to the forum
│   ├── handlers/
│   │   ├── handlers.py     # Classes for handling incoming requests
│   │   ├── __init__.py     # Initializes handler classes
│   ├── routers/
│   │   ├── routers.py      # Contains all aiogram routers
│   │   ├── __init__.py     # Imports all routers at once
```

The project follows **MVC** and **OOP** principles to ensure a clean and modular codebase.

---

## 💻 Installation and Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/atheop1337/wrp-bot.git
   cd wrp-bot
   ```

2. Install dependencies (use `aiosqlite`):
   ```bash
   pip install aiosqlite aiogram
   ```

3. Open `main.py` and insert your Telegram bot token:
   ```python
   TOKEN_FILE_PATH = 'your-telegram-bot-token'
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

---

## 📜 License

This project is licensed under the MIT License. See the full license [here](LICENSE).

![MIT License Badge](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 🧑‍💻 Author

- **GitHub:** [atheop1337](https://github.com/atheop1337)

Special thanks to **Natrix Xayten** for their help.

---

## 🛡️ Security

Keep your bot token secure and avoid hardcoding sensitive information in the source code. Use environment variables or a configuration file for sensitive data when deploying in production.

---

## 📚 How It Works

1. **Change flarum_remember:**  
   Users can change their `flarum_remember` token by clicking the **Change flarum** button in the bot. If no token is set, it defaults to `NULL`.

2. **Sending Messages:**  
   After setting their token, users can send messages to the forum by providing the discussion ID and message text.

3. **Database Interaction:**  
   The bot uses `aiosqlite` to store and manage user tokens. When a user changes their `flarum_remember`, the new token is saved in the database.
