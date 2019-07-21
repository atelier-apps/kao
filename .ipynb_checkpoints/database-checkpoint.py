import psycopg2
import os

DATABASE_URL = os.environ.get("DATABASE_URL")


def init_tables():
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("DROP TABLE images;")
            cur.execute("CREATE TABLE images(id int PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY, file_id text, result json, ip text, user_agent json, created_at timestamp);")
        conn.commit()

# データベース接続
def get_connection():
    return psycopg2.connect(DATABASE_URL, sslmode='require')

