from flask import Flask  # Import Flask to allow us to create our app.
app = Flask(__name__)    # Global variable __name__ tells Flask whether or not we are running the file

@app.route("/")
def helloworld():
    return "Hello World"

@app.route("/dojo")
def dojo():
    return "Dojo!"

@app.route("/say/<name>")
def say(name):
    return "Hi", name + "!"

@app.route("/repeat/<num>/<name>")
def hello(num,name):
    output=""
    for i in range(0,int(num),1):
        output+= name + " <br>"
    return output

app.run(debug=True, host="0.0.0.0",port=8080)
