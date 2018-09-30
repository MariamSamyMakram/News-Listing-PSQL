#!/usr/bin/env python
import psycopg2
from PrintTable import print_table


class DatabaseConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname='news')
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def select(self, q):
        self.cursor.execute(q)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()


if __name__ == '__main__':
    database_connection = DatabaseConnection()

    result1 = database_connection.select("select title , count(path)||' '||'views' as views" +
                                         " from articles ,log where path='/article/'||slug group by title " +
                                         "order by count(path) desc;")

    result2 = database_connection.select(
        "select authors.name, sum(views_table.views)||' '||'views' as sum_views from authors ," +
        " (select title, author, count(path) as views from articles ,log " +
        "where path='/article/'||slug group by title,author) as views_table" +
        " where authors.id = author group by authors.name order by sum(views_table.views) desc ;")

    result3 = database_connection.select(
        "SELECT time, percentage_error_value*100 FROM percentage_error" +
        " WHERE percentage_error.percentage_error_value > 0.01")

    database_connection.close()

    print('First Query\n')
    print_table(result1,
                header=["Title", "views"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)

    print('\nSecond Query\n')
    print_table(result2,
                header=["Title", "views"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)

    print('\nThird Query\n')
    print_table(result3,
                header=["Date", "Percentage"],
                wrap=True, max_col_width=30, wrap_style='wrap',
                row_line=True, fix_col_width=True)
