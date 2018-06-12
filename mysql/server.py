from flask import Flask, render_template, request, redirect, session, flash
from mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key = 'somekey'

mysql = connectToMySQL('mydb')

print("all the users", mysql.query_db("SELECT * FROM users;"))

@app.route('/')
def index():
    print("normal")
    print (session)
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template("index.html", count=session['count'])


@app.route('/checkout', methods=['POST'])
def checkout():
    if len(request.form['first_name']) < 1:
        flash("First name cannot be empty!")
    elif str.isalpha(request.form['first_name']) != True:
        flash("You are more than just a number.")
    else:
        flash(f"Success! Your first name is {request.form['first_name']}.") # just pass a string to the flash function

    if len(request.form['last_name']) < 1:
        flash("Last name cannot be empty!")
    elif str.isalpha(request.form['last_name']) != True:
        flash("You are more than just a number.")
    else:
        flash(f"Success! Your last name is {request.form['last_name']}.") # just pass a string to the flash function

    if len(request.form['email']) < 1:
        flash("Email cannot be empty!")
    elif EMAIL_REGEX.match(request.form['email']):
        flash("Doesn't look like an email address!")
    else:
        flash(f"Success! Your email is {request.form['email']}.") # just pass a string to the flash function

    if len(request.form['password']) < 7:
        flash("Password cannot be less than 8 characters!")
    else:
        if request.form['password']==request.form['passwordconf']:
            flash(f"Success! Your password is {request.form['password']}.") # just pass a string to the flash function
        else:
            flash("Passwords do not match!")
    return redirect('/')


    fname=request.form['first_name']
    lname=request.form['last_name']
    email=request.form['email']

    return render_template("checkout.html", fname=fname, lname=lname)


if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)