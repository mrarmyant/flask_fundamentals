from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file



@app.route("/<x>/<y>")
def makeCheckerBoard(x=8,y=8):
    return render_template("index.html", x=int(x), y=int(y))
app.run(debug=True, host="0.0.0.0",port=8080)