import psycopg2
import json
from logger import get_logger

logger = get_logger('data_base')


def check_connection():
    global conn, cur
    try:
        conn = psycopg2.connect(
            dbname='DB_FOR_BOT',
            user='Kyrtsun',
            password='Kirtsun123',
            host='db_bot',
            port='5432'
        )
        if conn:
            logger.info('Соиденение с базой прошло успешно.')
            cur = conn.cursor()
            sql_start()
    except psycopg2.Error as e:
        logger.critical(f'Подключение не произошло! {e}')


def sql_start():
    with conn:
        try:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS products ('
                'product_id SERIAL PRIMARY KEY,'
                'im1 TEXT NOT NULL,'
                'video TEXT NOT NULL,'
                'name TEXT NOT NULL,'
                'size INTEGER NOT NULL,'
                'sm FLOAT NOT NULL,'
                'condition INTEGER NOT NULL,'
                'price FLOAT NOT NULL)'
            )
            logger.info('Таблица продукты создана')
        except Exception as e:
            logger.critical(f'Таблица продукты не была созадана - {e}')
        try:
            cur.execute(
                'CREATE TABLE IF NOT EXISTS users ('
                'id SERIAL PRIMARY KEY,'
                'name TEXT NOT NULL,'
                'user_id INTEGER NOT NULL)')
            logger.info('Таблица юзеры создана')
            conn.commit()
        except Exception as e:
            logger.critical(f'Таблица юзеры не была создана - {e}')


async def save_post(data):
    videos = []
    photos = []
    info = {}
    for key, value in data.items():
        if key.startswith('photo'):
            photos.append(value)
        elif key.startswith('video'):
            videos.append(value)
        else:
            info[key] = value

    photo_json = json.dumps(photos)
    videos_json = json.dumps(videos)

    with conn:
        try:
            cur.execute('INSERT INTO products(im1, video, name, size, sm, condition, price)'
                        ' VALUES (%s, %s, %s, %s, %s, %s, %s)',
                        (photo_json, videos_json, info.get('name'), info.get('size'), info.get('sm'),
                         info.get('condition'), info.get('price')))

            if cur.rowcount > 0:
                logger.info('Информация сохранена')
                return True
            else:
                logger.info('Информация не была сохранена')
                return False

        except psycopg2.Error or Exception as e:
            logger.critical(f'Не удалось сохранить инфо - {e}')

        finally:
            conn.commit()


async def save_user_info(name, user_id):
    with conn:
        try:
            cur.execute('SELECT * FROM users WHERE user_id = %s', (user_id,))
            users = cur.fetchone()
            if not users:
                cur.execute('INSERT INTO users(name, user_id) VALUES (%s, %s)', (name, user_id))
                if cur.rowcount > 0:
                    logger.info('Юзер сохранен!')
                    return True
                else:
                    logger.info('Юзер сохранен!')
                    return False

        except psycopg2.Error as e:
            logger.critical(f'Юзер не был сохранен!{e}')
        finally:
            conn.commit()


async def get_size(size, sm):
    with conn:
        try:
            cur.execute('SELECT * FROM products WHERE size=%s and sm=%s', (size, sm))
            res = cur.fetchall()

            if res:
                return res
            else:
                return False
        except psycopg2.Error as e:
            logger.critical(f'Данные не были выгружены! {e}')


async def del_boots(pk):
    with conn:
        try:
            cur.execute('DELETE FROM products WHERE product_id=%s', (pk,))
            if cur.rowcount > 0:
                logger.info('Данные удалены!')
                return True
            else:
                logger.info('Данные не удалены!')
                return False
        except psycopg2.Error as e:
            logger.critical(f'Не удалось удалить пост! {e}')
        finally:
            conn.commit()
