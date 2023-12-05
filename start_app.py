import asyncio

from Data_base.database import check_connection

from aiogram.types.bot_command import BotCommand

from handlers import admin_del_router, admin_save_router, help_router, start_router, user_router

from loader import bot, dp

from logger import get_logger


logger = get_logger('start_app')


async def main():
    dp.include_routers(
        admin_save_router,
        admin_del_router,
        start_router,
        user_router,
        help_router,
    )
    try:
        await dp.start_polling(bot)
    except Exception as e:
        logger.critical(f'Не удалось запустить бота {e}')
    await bot.set_my_commands([BotCommand(command='/start', description='Показать стартовое сообщение.'),
                              BotCommand(command='/help', description='Показать список доступных команд.'),
                               BotCommand(command='/menu', description='Меню размеров.')])


if __name__ == "__main__":
    check_connection()
    asyncio.run(main())
