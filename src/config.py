# BOT CONFIG -------------------------
PREFIX = ','
DEVS = ("631744856259297286", "853094854683000894")
EXTENSIONS = ("cogs.esports", "cogs.mod", "cogs.misc", "cogs.utility", "cogs.reminder", "cogs.events", "server")#, "cogs.premium", "sockets")
SERVER_ID = ''
VOTER_ROLE = ''
PREMIUM_ROLE = ''


# BOT SIMPLIFIER -------------------------
BOT_NAME = 'Legion'
BOT_DOMAIN = 'rexz.ml'
COLOR = 0xff0000
FOOTER = 'innocent gang op'
DBL_TOKEN = 'h'
SERVER_LINK = 'https://discord.gg/rexzop'
PRO_LINK = 'https://discord.gg/rexzop'
PAY_LINK = 'https://lustrouswindingvertex.emanuelskirtzzz.repl.co/'
BOT_INVITE = 'https://discord.gg/rexzop'
REPOSITORY = "https://discord.gg/rexzop"
IMG = {
        'TGROUP': "https://media.discordapp.net/attachments/1095621025762381834/1095621079554330634/IMG_20230412_125507.jpg", 
        "ONETOFIFTY": "https://media.discordapp.net/attachments/1095621025762381834/1095622914939818006/IMG_20230412_134407.jpg",
        'TICKCROSS': " https://media.discordapp.net/attachments/1095621025762381834/1095639018642866257/IMG_20230412_144806.jpg", 
        'EZGIF': "", 
        'TIME': "",
}
PREMIUM_AVATAR = ''
PRIME_EMOJI = ""


# WEBSITE -------------------------
WEBSITE = "https://lustrouswindingvertex.emanuelskirtzzz.repl.co/"
FASTAPI_URL = 'https://lustrouswindingvertex.emanuelskirtzzz.repl.co/get_premium'
FASTAPI_KEY = 'venomexe'
PAYU_SALT = ''
PAYU_PAYMENT_LINK = ''
SERVER_PORT = '8080'
SOCKET_URL = 'https://lustrouswindingvertex.emanuelskirtzzz.repl.co/'
SOCKET_AUTH = 'dscsfgfwfd'


# DATABASE -------------------------
TORTOISE = {
    "connections": {
        "default": {
            "engine": "tortoise.backends.asyncpg",
            "credentials": {
                "host": "ziggy.db.elephantsql.com",
                "port": "5432",
                "user": "mlxyxsyh",
                "password": "t5IFqvPT2BQ0VLHWqk9Z5wPboSOHinoi",
                "database": "mlxyxsyh",
            },
        },
    },
    "apps": {
        "models": {
            "models": ["models"],#, "aerich.ini"],
            "default_connection": "default",
        },
    },
}


# LOGS -------------------------
SHARD_LOG = "https://discord.com/api/webhooks/1095403844856447088/FBBZ4ylvq-7qt5JAvDvZCUvgCHdypSSno0ggkddt677F2mq24MPyrOsaFyDTSNpeU3vY"
ERROR_LOG = "https://discord.com/api/webhooks/1095403844856447088/FBBZ4ylvq-7qt5JAvDvZCUvgCHdypSSno0ggkddt677F2mq24MPyrOsaFyDTSNpeU3vY"
PUBLIC_LOG = "https://discord.com/api/webhooks/1095403844856447088/FBBZ4ylvq-7qt5JAvDvZCUvgCHdypSSno0ggkddt677F2mq24MPyrOsaFyDTSNpeU3vY"