from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file

@app.route('/play')

def hello_world():
    return render_template("index.html")

@app.route("/play/<boxnum>/<color>")
def makeBoxes(boxnum,color):
    return render_template("index.html", boxnum=int(boxnum), color=color)
app.run(debug=True, host="0.0.0.0",port=8080)