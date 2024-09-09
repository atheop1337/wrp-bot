from modules.handlers.handlers import StartHandler, FlarumHandler, SenderHandler
from modules.libraries.utils import const

start_handler = StartHandler(const.DATABASE_NAME)
flarum_handler = FlarumHandler(const.DATABASE_NAME)
sender_handler = SenderHandler(const.DATABASE_NAME)
