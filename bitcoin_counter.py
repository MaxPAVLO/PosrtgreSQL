import psycopg2
from prettytable import from_db_cursor
from requests_html import HTMLSession
import datetime as dt

cur = None
conn = None

try:
	session = HTMLSession()
	r = session.get("https://ru.investing.com/crypto/bitcoin/btc-usd")

	article = r.html.find("span.text-2xl", first = True)
	headline = article.find(".text-2xl", first = True).text

	conn = psycopg2.connect(
		host = "localhost",
		dbname = "demo",
		user = "postgres",
		password = 256809,
		port = 5433)

	cur = conn.cursor()

	date = dt.datetime.now()
	str_date = str(date)

	create_script = """CREATE TABLE IF NOT EXISTS bitcoin(
			dates varchar(50),
			price varchar(100))"""

	cur.execute(create_script)

	insert_script = "INSERT INTO bitcoin VALUES(%s, %s)"
	insert_value = (str_date, headline)

	cur.execute(insert_script, insert_value)

	cur.execute("SELECT * FROM bitcoin")
	bitcoin_table = from_db_cursor(cur)
	
	print(bitcoin_table)

	conn.commit()

except Exception as error:
	print("ERROR")

finally:
	if cur is not None:
		cur.close()

	if conn is not None:
		conn.close()