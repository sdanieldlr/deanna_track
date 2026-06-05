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
            WHERE DATE(created) = CURDATE()) AS users_today,

            (SELECT COUNT(*)
            FROM cliperest_book
            WHERE DATE(created) = CURDATE()) AS ministores_today,

            (SELECT COALESCE(SUM(numViews),0)
            FROM cliperest_book
            WHERE DATE(created) = CURDATE()) AS views_today
    """)

    results = cursor.fetchone()

    cursor.close()
    connection.close()

    return {
        "users_today": results[0],
        "ministores_today": results[1],
        "views_today": int(results[2])
    }