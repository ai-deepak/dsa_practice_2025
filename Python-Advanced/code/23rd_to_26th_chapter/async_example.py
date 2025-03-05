from contextlib import asynccontextmanager

@asynccontextmanager
async def get_connection():
    conn = await acquire_db_connection()
    try:
        yield conn
    finally:
        await release_db_connection(conn)
    
async def get_all_user():
    async with get_connection() as conn:
        return conn.query('SELECT * FROM users')