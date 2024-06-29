#no need of it because this all this is done by sqlalcedmey 

#see lecture of the mam again 

from flask import Flask, render_template, request, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'mydb'

mysql = MySQL(app)

@app.route('/')
def index():
    name = 'Ayush chaurasia'
    password = '123'
    cur = mysql.connection.cursor()
    cur.execute('INSERT INTO USER(name, password) VALUES(%s, %s)', (name, password)) #user is table 
    mysql.connection.commit()
    cur.close()
    return make_response('Successfully stored data.')

if __name__ == '__main__':
    app.run(debug=True)
