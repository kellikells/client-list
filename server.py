
from flask import Flask, render_template, redirect, request, session, flash, jsonify
# import the function connectToMySQL from the file mysqlconnection.py
from mysqlconnection import connectToMySQL
app = Flask(__name__)
# invoke the connectToMySQL function and pass it the name of the database we're using
# connectToMySQL returns an instance of MySQLConnection, which we will store in the variable 'mysql'
mysql = connectToMySQL('clientsdb')
# now, we may invoke the query_db method
print("all the users", mysql.query_db("SELECT * FROM clients;"))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getData')
def getData():
    mysql = connectToMySQL("clientsdb")
    all_clients = mysql.query_db("SELECT * FROM clients")
    print("Fetched all clients", all_clients)

    return  jsonify(all_clients)


if __name__ == "__main__":
    app.run(debug=True)