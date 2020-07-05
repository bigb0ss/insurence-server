import mysql.connector as sql
from flask import Flask, jsonify,request
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
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
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
                row['vehicle_type']=t[6]
                row['mail']=t[7]
                row['address']=t[8]
                row['date']= t[9].strftime("%d-%m-%y")
                if (t[9])<(datetime.now()+timedelta(days=7)).date():
                        result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)




@app.route('/create',methods=['GET','POST'])
def createRecord():
        content = request.json
        print(content)
        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        if content['type'] =="1":
                query = "INSERT INTO private_vehicles(name,reference,contact,policy_number,policy_type,vehicle_type,mail,address,date) values (%s,%s,%s,%s,%s,%s,%s,%s,DATE %s)"
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type']=="2":
                query = "INSERT INTO heavy_vehicles(name,reference,contact,policy_number,policy_type,vehicle_type,mail,address,date) values (%s,%s,%s,%s,%s,%s,%s,%s,DATE %s)"
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type'] == "3":
                query = "INSERT INTO fire_misc(name,reference,contact,policy_number,policy_type,type,mail,address,date) values (%s,%s,%s,%s,%s,%s,%s,%s,DATE %s)"
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()

        return jsonify({"status":"success"})


@app.route('/renew',methods=['GET','POST'])
def renewRecord():
        content = request.json
        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        if content['type'] == "1":
                query ="UPDATE private_vehicles SET policy_number=%s,policy_type=%s,date=Date %s WHERE id = "+content['id']
                args = (content['policy_number'],content['policy_type'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type'] == "2":
                query ="UPDATE heavy_vehicles SET policy_number=%s,policy_type=%s,date=Date %s WHERE id = "+content['id']
                args = (content['policy_number'],content['policy_type'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type'] == "3":
                query ="UPDATE fire_misc SET policy_number=%s,policy_type=%s,date=Date %s WHERE id = "+content['id']
                args = (content['policy_number'],content['policy_type'],content['date'])
                db_cursor.execute(query,args)
                db_connection.commit()

        return jsonify({"status":"success"})

@app.route('/edit',methods=['GET','POST'])
def editRecord():
        content = request.json
        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        if content['type'] == "1":
                query= "UPDATE private_vehicles SET name=%s,reference=%s,contact=%s,policy_number=%s,policy_type=%s,vehicle_type=%s,mail=%s,address=%s WHERE id = "+content['id']
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type'] == "2":
                query= "UPDATE heavy_vehicles SET name=%s,reference=%s,contact=%s,policy_number=%s,policy_type=%s,vehicle_type=%s,mail=%s,address=%s WHERE id = "+content['id']
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'])
                db_cursor.execute(query,args)
                db_connection.commit()
        elif content['type'] == "3":
                query= "UPDATE fire_misc SET name=%s,reference=%s,contact=%s,policy_number=%s,policy_type=%s,type=%s,mail=%s,address=%s WHERE id = "+content['id']
                args = (content['name'],content['reference'],content['contact'],content['policy_number'],content['policy_type'],content['gtype'],content['mail'],content['address'])
                db_cursor.execute(query,args)
                db_connection.commit()

        return jsonify({"status":"success"})



@app.route('/search',methods=['GET','POST'])
def searchRecord():
        content = request.json
        db_connection = init_db()
        app.logger.info("Database Connection Established")
        db_cursor = db_connection.cursor()
        if content['type'] == "1":
                if content['search'] == "1":
                        query = "SELECT * FROM private_vehicles WHERE name like %s and policy_number like %s"
                        content['name'] = "%" + content['name'] + "%"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['name'],content['policy_number'])
                elif content['search'] == "2":
                        query = "SELECT * FROM private_vehicles WHERE name like %s and (date<=%s and date >=%s)"
                        content['name'] = "%"+content['name'] + "%"
                        args = (content['name'],content['date'],content['date'])
                elif content['search'] == "3":
                        query = "SELECT * FROM private_vehicles WHERE name like %s or name like %s"
                        content['name'] = "%" + content['name'] + "%"
                        args = (content['name'],content['name'])
                elif content['search'] == "4":
                        query = "SELECT * FROM private_vehicles WHERE policy_number like %s or policy_number like %s"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['policy_number'],content['policy_number'])
                elif content['search'] == "5":
                        query = "SELECT * FROM private_vehicles WHERE contact = %s or contact = %s"
                        args = (content['contact'],content['contact'])
                elif content['search'] == "6":
                        query = "SELECT * FROM private_vehicles WHERE date<=%s and date>=%s"
                        args = (content['date'],content['date'])

                db_cursor.execute(query,args)
                table_rows = db_cursor.fetchall()                 

        elif content['type'] == "2":
                if content['search'] == "1":
                        query = "SELECT * FROM heavy_vehicles WHERE name like %s and policy_number like %s"
                        content['name'] = "%" + content['name'] + "%"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['name'],content['policy_number'])
                elif content['search'] == "2":
                        query = "SELECT * FROM heavy_vehicles WHERE name like %s and (date<=%s and date >=%s)"
                        content['name'] = "%"+content['name'] + "%"
                        args = (content['name'],content['date'],content['date'])
                elif content['search'] == "3":
                        query = "SELECT * FROM heavy_vehicles WHERE name like %s or name like %s"
                        content['name'] = "%" + content['name'] + "%"
                        args = (content['name'],content['name'])
                elif content['search'] == "4":
                        query = "SELECT * FROM heavy_vehicles WHERE policy_number like %s or policy_number like %s"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['policy_number'],content['policy_number'])
                elif content['search'] == "5":
                        query = "SELECT * FROM heavy_vehicles WHERE contact = %s or contact=%s"
                        args = (content['contact'],content['contact'])
                elif content['search'] == "6":
                        query = "SELECT * FROM heavy_vehicles WHERE date<=%s and date>=%s"
                        args = (content['date'],content['date'])

                db_cursor.execute(query,args)
                table_rows = db_cursor.fetchall()

        elif content['type'] == "3":
                if content['search'] == "1":
                        query = "SELECT * FROM fire_misc WHERE name like %s and policy_number like %s"
                        content['name'] = "%" + content['name'] + "%"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['name'],content['policy_number'])
                elif content['search'] == "2":
                        query = "SELECT * FROM fire_misc WHERE name like %s and (date<=%s and date >=%s)"
                        content['name'] = "%"+content['name'] + "%"
                        args = (content['name'],content['date'],content['date'])
                elif content['search'] == "3":
                        query = "SELECT * FROM fire_misc WHERE name like %s or name like %s"
                        content['name'] = "%" + content['name'] + "%"
                        args = (content['name'],content['name'])
                elif content['search'] == "4":
                        query = "SELECT * FROM fire_misc WHERE policy_number like %s or policy_number like %s"
                        content['policy_number'] = "%" + content['policy_number'] + "%"
                        args = (content['policy_number'],content['name'])
                elif content['search'] == "5":
                        query = "SELECT * FROM fire_misc WHERE contact = %s or contact=%s"
                        args = (content['contact'],content['contact'])
                elif content['search'] == "6":
                        query = "SELECT * FROM fire_misc WHERE date<=%s and date>=%s"
                        args = (content['date'],content['date'])

                db_cursor.execute(query,args)
                table_rows = db_cursor.fetchall()


        result=[]
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
                #if (t[9])<(datetime.now()+timedelta(days=7)).date():
                result.append(row)
        app.logger.info("Results are processed ")
        return jsonify(result)


if __name__ == '__main__':
	app.run()
