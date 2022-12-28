import logging
logging.basicConfig(level=logging.WARNING,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

import pyrogram, os

if __name__ == "__main__" :
    plugins = dict(
        root="plugins"
    )
    app = pyrogram.Client(
        "bot",
        bot_token=os.environ.get("5811923357:AAFf-XotoOzFK_UOrpLF7o07N3ZyyBSuKiM"),
        api_id=int(os.environ.get("11912804")),
        api_hash=os.environ.get("3ede7ccee042fee943f8731f525508fc"),
        plugins=plugins
    )
    app.run()
