import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.redis import RedisStorage

from dotenv import load_dotenv

load_dotenv()

admins = [546439620, 465659759]

storage = RedisStorage.from_url('redis://redis:6379/0')
dp = Dispatcher(storage=storage)
bot = Bot(os.getenv("API"))
