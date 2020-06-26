import mysql.connector as sql
from flask import Flask, jsonify
from datetime import timedelta, datetime 
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
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
                #if (t[9])>(datetime.now()+timedelta(days=7)).date():
                result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)


@app.route('/renew_vehicle')
def getRenewVechile():

        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * FROM private_vehicles')
        table_rows = db_cursor.fetchall()
        app.logger.info("Results fetched from Database")
        result =[]
        for t in table_rows:
                row={}
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
                if (t[9])<(datetime.now()+timedelta(days=7)).date():
                        result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)




@app.route('/mvehicle')
def getMVechile():

        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * FROM heavy_vehicles')
        table_rows = db_cursor.fetchall()
        app.logger.info("Results fetched from Database")
        result =[]
        for t in table_rows:
                row={}
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
                #if (t[9])>(datetime.now()+timedelta(days=7)).date():
                result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)


@app.route('/renew_mvehicle')
def getRenewMVechile():

        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * FROM heavy_vehicles')
        table_rows = db_cursor.fetchall()
        app.logger.info("Results fetched from Database")
        result =[]
        for t in table_rows:
                row={}
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
                if (t[9])<(datetime.now()+timedelta(days=7)).date():
                        result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)




@app.route('/fire_misc')
def getFireMisc():

        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * FROM fire_misc')
        table_rows = db_cursor.fetchall()
        app.logger.info("Results fetched from Database")
        result =[]
        for t in table_rows:
                row={}
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                #row['vehicle_type']=t[6]
                row['mail']=t[6]
                row['address']=t[7]
                row['date']= t[8].strftime("%d-%m-%y")
                #if (t[8])>(datetime.now()+timedelta(days=7)).date():
                result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)


@app.route('/renew_fire_misc')
def getRenewFireMisc():

        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        db_cursor.execute('SELECT * FROM fire_misc')
        table_rows = db_cursor.fetchall()
        app.logger.info("Results fetched from Database")
        result =[]
        for t in table_rows:
                row={}
                row['id']=str(t[0])
                row['name']=t[1]
                row['reference']=t[2]
                row['contact']=t[3]
                row['policy_number']=t[4]
                row['policy_type']=t[5]
                #row['vehicle_type']=t[6]
                row['mail']=t[6]
                row['address']=t[7]
                row['date']= t[8].strftime("%d-%m-%y")
                if (t[8])<(datetime.now()+timedelta(days=7)).date():
                        result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)




@app.route('/create',methods=['GET','POST'])
def createRecord():
        content = request.json
        print(content)
        if content['type'] ==1:
                pass
        elif content['type']==2:
                pass
        elif content['type'] == 3:
                pass 

        return jsonify({"status":"success"})

if __name__ == '__main__':
	app.run()
