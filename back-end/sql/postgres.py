import psycopg2
from pydantic import BaseModel


class Postgres(BaseModel):

    def conect_postgres():
        connect = psycopg2.connect(
            database='contacts', host='localhost', user='postgres', password='custelinha')
        cursor = connect.cursor()
        return cursor

    def get_contacts_postgres(query):
        connect = Postgres.conect_postgres()
        connect.execute(query)
        return connect.fetchall()

    def post_contacts_postgres(query):
        connect = Postgres.conect_postgres()
        connect.execute(query)

    def post_delete_postgres(query):
        connect = Postgres.conect_postgres()
        connect.execute(query)

    def post_update_postgres(query):
        connect = Postgres.conect_postgres()
        connect.execute(query)
