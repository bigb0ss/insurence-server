import mysql.connector as sql
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/vehicle',methods)
def getVechile():

	host = 'sql12.freemysqlhosting.net'
	database = 'sql12346844'
	user = 'sql12346844'
	password = '7TfAdTJn6R'

	db_connection = sql.connect(host=host,database=database,user=user,password=password)

	db_cursor = db_connection.cursor()
	db_cursor.execute('SELECT * FROM private_vehicles')
	table_rows = db_cursor.fetchall()
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

	return jsonify(result)


if __name__ == '__main__':
	app.run()