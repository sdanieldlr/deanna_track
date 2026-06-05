import os
import pymysql
from dotenv import load_dotenv

load_dotenv()

def get_data():
    connection = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_DATABASE")
    )

    cursor = connection.cursor()

    cursor.execute("""
        SELECT
        
            (SELECT COUNT(*)
            FROM cliperest_user
            WHERE DATE(created) = CURDATE() - INTERVAL 1 DAY) AS users,

            (SELECT COUNT(*)
            FROM cliperest_book
            WHERE DATE(created) = CURDATE() - INTERVAL 1 DAY) AS ministores,

            (SELECT COALESCE(SUM(numViews),0)
            FROM cliperest_book
            WHERE DATE(created) = CURDATE() - INTERVAL 1 DAY) AS views
    """)

    results = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "users": results[0],
        "ministores": results[1],
        "views": int(results[2])
    }