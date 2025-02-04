import asyncio ,logging
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import async_main

bot = Bot(token='7586884677:AAFhmeSRHaU3SvG4fjFFNbSccBN7GwVidkI')
dp = Dispatcher()

async  def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
  try:
    asyncio.run(main())
  except KeyboardInterrupt:
     print('Bot vyklychen')
