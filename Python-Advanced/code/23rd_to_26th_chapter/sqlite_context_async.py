import asyncio
import logging

import aiosqlite

async def main():
    logging.basicConfig(level=logging.INFO)
    async with aiosqlite.connect('example.db') as db:
        async with db.execute('SELECT * FROM users') as cursor:
            logging.info(await cursor.fetchall())

if __name__ == '__main__':
    asyncio.run(main())