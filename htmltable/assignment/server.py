from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file



@app.route("/")
def htmlTable():
    users = (
       {'first_name' : 'Michael', 'last_name' : 'Choi'},
       {'first_name' : 'John', 'last_name' : 'Supsupin'},
       {'first_name' : 'Mark', 'last_name' : 'Guillen'},
       {'first_name' : 'KB', 'last_name' : 'Tonel'}
    );
    return render_template("index.html", users=users)
app.run(debug=True, host="0.0.0.0",port=8080)