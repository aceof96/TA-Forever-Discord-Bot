# 🎮 TA-Forever Discord Bot
![TAF Logo]![image](https://github.com/user-attachments/assets/b6c512fd-9fa3-4297-860a-f11f74189c31)

This bot tracks for new games played by TAF players addeand to the bots list and posts results to the inputed Discord channel.

---

## 📋 Features

- Monitors TA-Forever API for new matches by tracked players
- Posts detailed match results and map previews to Discord
- Commands to dynamically add or remove users from tracking

---

## 🚀 Setup Instructions

### 1. Clone this repository


git clone https://github.com/your-username/TA-Forever-Discord-Bot.git
cd TA-Forever-Discord-Bot
## 🔧 Setup

1. Clone or download this repo.
2. Create a virtual environment: python -m venv venv
3. Activate it: .\venv\Scripts\Activate
4. Install dependencies: pip install -r requirements.txt
5.  Create a .env file
In the root directory, add the following environment variables:
     <br/>DISCORD_TOKEN="your_discord_bot_token"
     <br/>DISCORD_CHANNEL=123456789012345678  # Replace with your Discord channel ID (no quotes)

▶️ Running the Bot
     <br/>To start the bot:
     <br/>python main.py
     💬 Bot Commands
     Command	Description
     $hello	Confirms bot is running
     $AddUserbyName username	Add a player to track
     $DelUserbyName username	Remove a player from tracking
     🛠️ TODO
      Improve stability and error handling
          <br/>Enhance user input validation
          <br/>Customize match result formatting
          <br/>Add better logging and debugging tools

🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or improve.
🙏 Acknowledgments
TA-Forever https://www.taforever.com/
discord.py https://discordpy.readthedocs.io/en/stable/
   ```bash
   python -m venv venv

launch the bot with python main.py
<br/>  To confirm the bot is running you can type $hello into the chat and the bot should reply with Hello!
<br/>  Type $AddUserbyName ExampleUsername into chat in order to add a uuser to track
<br/>  Type $DelUserbyName ExampleUsername into the chat to remove a player from tracking

### TODO:
<br/>  Stabilty updates
<br/>  Input satation updates
<br/>  Adjust the output format of games into discord pending communty input
```bash
