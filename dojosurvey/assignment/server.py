from flask import Flask, render_template  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file



@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=['POST'])
def result():
    print (request.form['name'])
    print (request.form['loc'])

    return render_template("results.html", name=request.form['name'], loc=request.form['loc'])
app.run(debug=True, host="0.0.0.0",port=8080)