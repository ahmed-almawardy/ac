from psycopg2 import connect, sql
from faker import Faker
from random import randint
from copy import copy
from timeit import timeit

DB_OPTIONS = {
    "host": "localhost",
    "dbname": "local_db",
    "user": "postgres",
    "password": "password",
}

conn = connect(**DB_OPTIONS)
conn.autocommit = True


class User:
    def __init__(self, username, email) -> None:
        self.username = username
        self.email = email


user = User(username="Default", email="default@app.com")
faker = Faker("en_US")


def gen_users2(times):
    for _ in range(times):
        yield User(faker.unique.name(), faker.unique.email())


with conn.cursor() as cur:
    times = 1000_00
    sqls = []
    for user in gen_users2(times):
        sqls.append([user.username, user.email])

    cur.execute("DELETE FROM users;")
    cur.executemany("INSERT INTO users VALUES (DEFAULT, %s,%s)", sqls)
    conn.commit()
