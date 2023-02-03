import os

class Config(object):

      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5484278199:AAF9jJuLtDkx1M4QsPJim9KPwaoWCBltO3A")
      API_ID = int(os.environ.get("API_ID", 4682685))
      API_HASH = os.environ.get("API_HASH",'3eba5d471162181b8a3f7f5c0a23c307')
      OWNER_ID = int(os.environ.get("OWNER_ID",945284066))

