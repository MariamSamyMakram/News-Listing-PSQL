#!/usr/bin/env python
import psycopg2
from PrintTable import print_table
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
    Result1 = database_connection.select(
        "select title , count(title)||' '||'views' as views from articles ,log" +
        " where path='/article/'||slug group by title order by views desc")

    Result2 = database_connection.select(
        "select authors.name, sum(views_table.views)||' '||'views' as  sum_views " +
        "from authors , (select title, author, count(path) as views " +
        "from articles ,log where path='/article/'||slug group by title,author) as views_table" +
        " where authors.id = author group by authors.name order by sum_views desc")

    Result3 = database_connection.select(
        "select  to_char(Date(time), 'Mon-dd-YYYY') as date, (count(time) * 100 / (select count(*) from log where status != '200 ok'))||'% '||'errors'" +
        " as percentage from log where status != '200 ok' " +
        " GROUP BY Date(time) HAVING (count(time) * 100 / (select count(*) from log where status != '200 ok')) > 1")

    print('First Query\n')
    print_table(Result1,
                header=["Title", "views"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)

    print('\nSecond Query\n')
    print_table(Result2,
                header=["Title", "views"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)

    print('\nThird Query\n')
    print_table(Result3,
                header=["date", "percentage"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)
