import logging
import sqlite3
from contextlib import contextmanager


@contextmanager
def open_db(filename: str):
    connection = sqlite3.connect(filename)
    try:
        logging.info("Creating a connection")
        yield connection.cursor()
    finally:
        logging.info("Closing the connection")
        connection.commit()
        connection.close()

def main():
    logging.basicConfig(level=logging.INFO)
    with open_db("application.db") as cursor:
        x = 3
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())
    print(cursor)

if __name__ == "__main__":
    main()