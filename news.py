import psycopg2
from pprint import pprint


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname='news')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except:
            pprint("database not connect")

    def select(self, q):
        self.cursor.execute(q)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    database_connection = DatabaseConnection()

    print database_connection.select("select title , count(path)||' '||'views' as views from articles ,log where path='/article/'||slug group by title order by views desc;")

    print database_connection.select("select authors.name, sum(views_table.views) as sum_views from authors , (select title, author, count(path) as views from articles ,log where path='/article/'||slug group by title,author) as views_table where authors.id = author group by authors.name order by sum_views desc ;")

    print database_connection.select("select DATE(time) as date from log where status != '200 ok'  GROUP BY date HAVING (count(time) * 100 / (select count(*) from log where status != '200 ok')) > 1;")

    database_connection.close()

