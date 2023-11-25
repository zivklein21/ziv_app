import psycopg2

def authentication(username, password):
    try:
        connection = psycopg2.connect(database='ziv', user='ziv', password='ziv' host='postgresql')
        cur = connection.cursor()
        cur.execute("select * from users where username='{0}' and password='{1};".format(username,password))
        return cur.fetchall()

    except:
        print("Error while connecting to PostgreSQL")


if __name__ == '__main__':
    print('hello')