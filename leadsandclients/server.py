from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'somekey'

mysql = connectToMySQL('customersdb')

@app.route('/')
def index():
    all_customers = mysql.query_db("SELECT * FROM customer")
    print("Fetched All customers", all_customers)
    return render_template("index.html", customers=all_customers)

@app.route('/del', methods=['POST'])
def deluser():
    query= ("DELETE FROM customer where id=" +request.form['id'])
    print ("======================================================")
    print (request.form['id'])
    print (query)
    mysql.query_db(query)
    return redirect("/")

@app.route('/editusers', methods=['POST'])
def editusers():
    print (request.form)
    return redirect("/")

@app.route('/customers', methods=['POST'])
def create():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
    elif str.isalpha(request.form['first_name']) != True:
        flash("You are more than just a number.")

    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif str.isalpha(request.form['last_name']) != True:
        flash("You are more than just a number.")

    query="INSERT INTO customer (first_name, last_name, leads, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(leads)s, NOW(), NOW());"
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'leads': int(request.form['leads'])
    }

    mysql.query_db(query,data)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)