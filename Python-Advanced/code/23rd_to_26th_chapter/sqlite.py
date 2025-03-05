import logging
import sqlite3

#without context manager
# def main():
#     logging.basicConfig(level=logging.INFO)
#     connection = sqlite3.connect("application.db")
#     try:
#         cursor = connection.cursor()
#         cursor.execute("SELECT * FROM blogs")
#         logging.info(cursor.fetchall())
#     finally:
#         connection.close()

#with context manager
def main():
    logging.basicConfig(level=logging.INFO)
    with sqlite3.connect("application.db") as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM blogs")
        logging.info(cursor.fetchall())


if __name__ == "__main__":
    main()

