import psycopg2
from pprint import pprint


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname='news')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error
            print(error)

    def select(self, q):
        self.cursor.execute(q)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    database_connection = DatabaseConnection()

    print database_connection.select("select title , count(path)||' '||'views' as views from articles ,log where path='/article/'||slug group by title order by count(path) desc;")

    print database_connection.select("select authors.name, sum(views_table.views) as sum_views from authors , (select title, author, count(path) as views from articles ,log where path='/article/'||slug group by title,author) as views_table where authors.id = author group by authors.name order by sum(views_table.views) desc ;")

    print database_connection.select( "SELECT * FROM percentage_error WHERE percentage_error.percentage_error_value > 0.01")

    database_connection.close()

