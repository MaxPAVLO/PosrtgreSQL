import psycopg2

hostname = "localhost"
database = "demo"
username = "postgres"
pwd = 256809
port_id = 5433
conn = None
cur = None

try:

	conn = psycopg2.connect(
		host = hostname,
		dbname = database,
		user = username,
		password = pwd,
		port = port_id)

	cur = conn.cursor()

	create_script = """CREATE TABLE IF NOT EXISTS eml(
	id int PRIMARY KEY,
	name varchar(40) NOT NULL,
	salary int,
	dept_id varchar(30))"""

	cur.execute(create_script)

	insert_script = "INSERT INTO eml (id, name, salary, dept_id) VALUES (%s, %s, %s, %s)"
	insert_value = [(1, "Sam", 12000, "D1"), (2, "James", 20000, "A9"), (3, "Bob", 21000, "L5"), (4, "Max", 56000, "H8"), (5, "Ben", 26000, "O7")]
	insert_value_num2 = [(6, "Jeam", 11000, "R3"), (7, "Laura", 15000, "Q9"), (8, "Ron", 20000, "K4"), (9, "Will", 35000, "Z5"), (10, "Sam", 49000, "P5")]

	#for record in insert_value_num2:
		#cur.execute(insert_script, record)

	cur.execute("SELECT * FROM EML")
	for record in cur.fetchall():
		print(record[1], record[2], record[3])

	conn.commit()

except Exception as error:
	print("ERROR")

finally:
	if cur is not None:
		cur.close()

	if conn is not None:
		conn.close()
		