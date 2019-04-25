import MySQLdb
import os

def hello():
    conn = MySQLdb.connect(host='rds-reader3-readreplica.cot6ghx0ckt3.us-east-1.rds.amazonaws.com',
                                user='mds',
                                passwd=os.environ['READ_DB_PASSWORD'],
                                db='reader',
                                autocommit=True)
    c = conn.cursor()

    sql = '''SELECT * FROM read_entrez_article LIMIT 1'''
    c.execute(sql, ())
    print(c.fetchone())
    c.close()

hello()