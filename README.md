# TA-Forever-Discord-Bot
![image](https://github.com/user-attachments/assets/b6c512fd-9fa3-4297-860a-f11f74189c31)

This bot tracks for new games played by TAF players addeand to the bots list and posts results to the inputed Discord channel.

## 🔧 Setup

1. Clone or download this repo.
2. Create a virtual environment:
3. Create a .env file and add the below 2 variables
     DISCORD_TOKEN = "insert your generated discord token within these quotation marks"
     DISCORD_CHANNEL = insert the desired channels ID
   
   ```bash
   python -m venv venv

launch the bot with python main.py
  To confirm the bot is running you can type $hello into the chat and the bot should reply with Hello!
  Type $AddUserbyName ExampleUsername into chat in order to add a uuser to track
  Type $DelUserbyName ExampleUsername into the chat to remove a player from tracking

### TODO:
<br/>  Stabilty updates
<br/>  Input satation updates
<br/>  Adjust the output format of games into discord pending communty input
