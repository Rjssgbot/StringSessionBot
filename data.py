from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("ð· Start Generating Session ð·", callback_data="generate")]

    home_buttons = [
        generate_single_button,
        [InlineKeyboardButton(text="ð¹Return Homeð¹", callback_data="home")]
    ]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("ð« Bot Status and More Bots ð«", url="https://t.me/RomeoBot_OP")],
        [
            InlineKeyboardButton("ð¹How to Use âð¹", callback_data="help"),
            InlineKeyboardButton("ð¹ About ð¹", callback_data="about")
        ],
    ]

    START = """
Hey {}

Welcome to {}

If you don't trust this bot, 
1) stop reading this message
2) delete this chat

Still reading?
You can use me to generate pyrogram (even version 2) and telethon string session. Use below buttons to learn more !

By @RJssgbot
    """

    HELP = """
â¨ **Available Commands** â¨

/about - About The Bot
/help - This Message
/start - Start the Bot
/generate - Generate Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    ABOUT = """
**About This Bot** 

Telegram Bot to generate Pyrogram and Telethon string session by @Rjssgbot
                
Framework : [Pyrogram](https://docs.pyrogram.org)

Language : [Python](https://www.python.org)

Developer : ð¾ð¡ï¸ðï¸ðï¸ð¾
    """
