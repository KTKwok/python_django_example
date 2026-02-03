import os
from mysql.connector import connect, Error
from dotenv import load_dotenv

# Load Environment from .env
load_dotenv()

if __name__ == '__main__':
    try:
        with connect(
            host=os.getenv('DB_HOST'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PWD'),
            database=os.getenv('DB_DATABASE'),
        ) as connection:
            print(connection)
            read_table_query = """
               SELECT * FROM world.city;
            """

            with connection.cursor() as cursor:
                cursor.execute(read_table_query)
                result = cursor.fetchall()
                for row in result:
                    print(row)
    except Error as e:
        print(e)