from os import getenv

class Config(object):
      API_HASH = getenv("API_HASH", "dae4b28e14b51583475a8def6ca06934")
      API_ID = int(getenv("API_ID", "22179988"))
      AS_COPY = True if getenv("AS_COPY", True) == "`{file_name}`" else True
      BOT_TOKEN = getenv("BOT_TOKEN", "6970656817:AAEzIuiq4aKmq95PGsDRc4UGjeb_HPT9lWs")
      CHANNEL = list(x for x in getenv("CHANNEL_ID", "-1001960613454:-1001564274544").replace("\n", " ").split(' '))


# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
