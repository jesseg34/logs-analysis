#!/usr/bin/env python3
import psycopg2

top_three_articles_report = {
    "title": "Most popular three articles of all time.",
    "query": """select articles.title, count(*) as views
                from articles,
                log
                where log.path = concat('/article/', articles.slug)
                group by articles.title
                order by views desc limit 3"""
}

top_authors_by_views_report = {
    "title": "Most popular article authors of all time.",
    "query": """select authors.name, count(*) as views
                from articles
                inner join authors on articles.author = authors.id
                inner join log on log.path = concat('/article/', articles.slug)
                group by authors.name
                order by views desc"""
}

days_with_1_perc_err_report = {
    "title": "Days with more than 1% of requests with errors",
    "query": """Select dayErrors.totalsDay,
                ROUND(dayErrors.errorLogCount::NUMERIC/dayErrors.logCount*100.0, 2)
                ||'%' AS rate
                FROM
                ((
                    select CAST(time as DATE) as totalsDay,
                    count(*) as logCount
                    from log
                    group by totalsDay
                ) AS totalLogs
                JOIN
                (
                    select CAST(time as DATE) as errorsDay,
                    count(*) as errorLogCount
                    from log
                    where status like '%'||'404'||'%'
                    group by errorsDay
                ) AS errorLogs
                ON totalLogs.totalsDay = errorLogs.errorsDay
                ) AS dayErrors
                WHERE
                (dayErrors.errorLogCount::NUMERIC/dayErrors.logCount) > 0.01"""
}


def get_query_results(query):
    """ Executes a specified query and returns results. """
    db, cursor = connect()
    cursor.execute(query)
    results = cursor.fetchall()
    db.close()
    return results, cursor.description


def print_report(report):
    """ Print the results of a report query. """
    query_results = get_query_results(report["query"])
    print(report["title"])
    for index, results in enumerate(query_results[0]):
        print("{}. {} - {} {}"
              .format(index+1, results[0], results[1], query_results[1][1][0]))
    return


def connect(db_name="news"):
    """ Connects to database and returns connection. """
    try:
        db = psycopg2.connect("dbname={}".format(db_name))
        cursor = db.cursor()
        return db, cursor
    except psycopg2.DatabaseError:
        print("Unable to connect to the database")


if __name__ == '__main__':
    # Print reports
    print_report(top_three_articles_report)
    print_report(top_authors_by_views_report)
    print_report(days_with_1_perc_err_report)
