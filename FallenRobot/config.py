class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    API_ID = 17763538
    API_HASH = "babad31b4b434fc53d8bd13370c556c3"

    CASH_API_KEY = "9VTTT9B4QHV8DIDS"  # Get this value for currency converter from https://www.alphavantage.co/support/#api-key

    DATABASE_URL = ""  # A sql database url from elephantsql.com

    EVENT_LOGS = (-1002108743436)  # Event logs channel to note down important bot level events

    MONGO_DB_URI = "mongodb+srv://nakuldkdhacker:nakuldkdhacker$100@cluster0.45znzoj.mongodb.net/"  # Get ths value from cloud.mongodb.com

    # Telegraph link of the image which will be shown at start command.
    START_IMG = "https://files.catbox.moe/jxk5hn.jpg"

    SUPPORT_CHAT = "THE_FUCKER_BOTS_2926"  # Your Telegram support group chat username where your users will go and bother you

    TOKEN = "6894743901:AAFlsaTrSwxaFpYMVXeXpkbr3NR_Nimoepw"  # Get bot token from @BotFather on Telegram

    TIME_API_KEY = "A8RZUCKYOVRS"  # Get this value from https://timezonedb.com/api

    OWNER_ID = 6961211249  # User id of your telegram account (Must be integer)

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8


class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
