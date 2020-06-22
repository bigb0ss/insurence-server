import mysql.connector as sql
from flask import Flask, jsonify

import logging

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def index():
	return "<h1> API is Online </h1>"


def init_db():
        host = 'remotemysql.com'
	database = 'JZrbXapnEH'
	user = 'JZrbXapnEH'
	password = 'A8RONVZxmh'
        db_connection = sql.connect(host=host,database=database,user=user,password=password)
        return db_connection
        
	

@app.route('/vehicle')
def getVechile():

	db_connection = init_db()
	app.logger.info("Database Connection Established")
	db_cursor = db_connection.cursor()
	db_cursor.execute('SELECT * FROM private_vehicles')
	table_rows = db_cursor.fetchall()
	app.logger.info("Results fetched from Database")
	result =[]
	for t in table_rows:
		row={}
		row['id']=t[0]
		row['name']=t[1]
		row['reference']=t[2]
		row['contact']=t[3]
		row['policy_number']=t[4]
		row['policy_type']=t[5]
		row['vehicle_type']=t[6]
		row['mail']=t[7]
		row['address']=t[8]
		row['date']= t[9]

		result.append(row)
	app.logger.info("Results are processed ")
	return jsonify(result)


if __name__ == '__main__':
	app.run()
