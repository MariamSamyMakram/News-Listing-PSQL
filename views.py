#!/usr/bin/env python
import psycopg2

db = psycopg2.connect(dbname="news")
c = db.cursor()


ERROR_COUNTS_BY_DAY = '''
    CREATE OR REPLACE VIEW daily_error_view AS
        SELECT time::date, COUNT(*) AS Error_Count
        FROM log
        WHERE status != '200 OK'
        GROUP BY time::date
        ORDER BY time::date DESC;
'''

REQUEST_COUNT_BY_DAY = '''
    CREATE OR REPLACE VIEW daily_request_view AS
        SELECT time::date, COUNT(*) AS request_count
        FROM log
        GROUP BY time::date
        ORDER BY time::date DESC;
'''

PERCENT_ERROR = '''
    CREATE OR REPLACE VIEW percentage_error AS
    SELECT
        daily_error_view.time::date,
        CAST(daily_error_view.Error_Count AS FLOAT) /
            CAST(daily_request_view.request_count AS FLOAT)
            AS percentage_error_value
    FROM daily_error_view
    INNER JOIN daily_request_view
    ON daily_error_view.time::date=daily_request_view.time::date
    GROUP BY daily_error_view.time::date, daily_error_view.Error_Count,
    daily_request_view.request_count;
'''


c.execute(ERROR_COUNTS_BY_DAY)
c.execute(REQUEST_COUNT_BY_DAY)
c.execute(PERCENT_ERROR)
db.commit()
db.close()
