from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'somekey'

mysql = connectToMySQL('friendsdb')

print("all the users", mysql.query_db("SELECT * FROM users;"))

@app.route('/')
def index():
    all_friends = mysql.query_db("SELECT * FROM friends")
    print("Fetched All friends", all_friends)
    return render_template("index.html", friends=all_friends)

@app.route('/create_friend', methods=['POST'])
def create():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
    elif str.isalpha(request.form['first_name']) != True:
        flash("You are more than just a number.")

    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif str.isalpha(request.form['last_name']) != True:
        flash("You are more than just a number.")

    if len(request.form['occupation']) < 1:
        flash("Email cannot be empty!")

    query="INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW(), NOW());"
    data = {
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'occupation': request.form['occupation']
    }

    mysql.query_db(query,data)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)