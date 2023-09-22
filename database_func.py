import psycopg2

cnx = psycopg2.connect(
    user="chnrv",
    password="sih12345$",
    host="chnrv.postgres.database.azure.com",
    port=5432,
    database=""
)

cursor = cnx.cursor()


create_table_sql = """
CREATE TABLE newss (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    domain TEXT NOT NULL,
    published_date TEXT NOT NULL,
    tonality TEXT NOT NULL,
    content TEXT NOT NULL,
);
"""

# cursor.execute(create_table_sql)


news_data = {
    "id": "test_id",
    "title": "test_title",
    "domain": "test_domain",
    "published_date": "test_published_date",
    "tonality": "test_tonality",
    "content": "test_content"
}


def addItem(news_data):
    cnx = psycopg2.connect(
    user="chnrv",
    password="sih12345$",
    host="chnrv.postgres.database.azure.com",
    port=5432,
    database=""
    )

    cursor = cnx.cursor()

    insert_sql = """
    INSERT INTO newsNew (id, title, domain, published_date, tonality) VALUES (%s, %s, %s, %s, %s);
    """

    cursor.execute(insert_sql, (news_data["id"], news_data["title"],
                   news_data["domain"], news_data["published_date"], news_data["tonality"]))
    
    
    cnx.commit()
    cursor.close()
    cnx.close()

    return True

def queryTonality(tonality):
    cnx = psycopg2.connect(
    user="chnrv",
    password="sih12345$",
    host="chnrv.postgres.database.azure.com",
    port=5432,
    database=""
    )

    cursor = cnx.cursor()
    

    select_sql = """
    SELECT * FROM newsNew WHERE tonality = %s;
    """
    cursor.execute(select_sql, (tonality,))

    rows = cursor.fetchall()
    
    cnx.commit()
    cursor.close()
    cnx.close()

    return rows

def noOfTonality(tonality):
    cnx = psycopg2.connect(
    user="chnrv",
    password="sih12345$",
    host="chnrv.postgres.database.azure.com",
    port=5432,
    database=""
    )
    cursor = cnx.cursor()

    select_sql = """
    SELECT COUNT(*) FROM newsNew WHERE tonality = %s;
    """
    cursor.execute(select_sql, (tonality,))
    count = cursor.fetchall()

    cnx.commit()
    cursor.close()
    cnx.close()

    return count

def queryAll():
    cnx = psycopg2.connect(
    user="chnrv",
    password="sih12345$",
    host="chnrv.postgres.database.azure.com",
    port=5432,
    database=""
    )
    cursor = cnx.cursor()

    select_sql = """
    SELECT * FROM newsNew;
    """
    cursor.execute(select_sql)
    rows = cursor.fetchall()

    cnx.commit()
    cursor.close()
    cnx.close()

    return rows

def updateBasedOnId(row):
    update_sql = """
    UPDATE newsNew SET title = %s, domain = %s, published_date = %s, tonality = %s where id = %s;"""
    cursor.execute(update_sql, (row["title"], row["domain"], row["published_date"], row["tonality"], row["id"]))
    return True



cnx.commit()
cursor.close()
cnx.close()

