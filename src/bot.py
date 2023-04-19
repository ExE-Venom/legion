import os
if __name__ == "__main__":
    from core import bot

    bot.run(os.environ['token'])
