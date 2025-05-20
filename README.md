# 🎮 TA-Forever Discord Bot
![TAF Logo]![image](https://github.com/user-attachments/assets/b6c512fd-9fa3-4297-860a-f11f74189c31)

This bot tracks for new games played by TAF players addeand to the bots list and posts results to the inputed Discord channel.

---

## 📋 Features

- ⏱ Real-time monitoring of TA-Forever games
- 🧠 Detects wins/losses, maps, and player names
- 🖼 Posts map preview image and game details
- 💬 Commands to manage tracked users

---

## 🚀 Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/TA-Forever-Discord-Bot.git
cd TA-Forever-Discord-Bot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

#### On Windows PowerShell:
```powershell
.\venv\Scripts\Activate
```

#### On macOS/Linux:
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file in the root directory

```env
DISCORD_TOKEN="your_discord_bot_token"
DISCORD_CHANNEL=123456789012345678
```

> 📝 Replace the values with your actual bot token and target Discord channel ID.

---

## ▶️ Running the Bot

After completing setup, launch the bot with:

```bash
python main.py
```

---

## 💬 Bot Commands

| Command                      | Function                                 |
|-----------------------------|------------------------------------------|
| `$hello`                    | Confirms the bot is online               |
| `$AddUserbyName <username>` | Adds a player to be tracked              |
| `$DelUserbyName <username>` | Removes a tracked player                 |

---

## 📁 Project Structure

```
.
├── main.py
├── GameList.py
├── Users.py
├── requirements.txt
├── .env
└── README.md
```

---

## 🛠 TODO

- [ ] Improve error handling and bot stability
- [ ] Enhance user input validation
- [ ] Support multi-game posting and formatting
- [ ] Add logging and better debugging support

---

## 🤝 Contributing

Contributions are welcome! Please open an issue or pull request with proposed changes, ideas, or enhancements.

---

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## 🙏 Acknowledgments
