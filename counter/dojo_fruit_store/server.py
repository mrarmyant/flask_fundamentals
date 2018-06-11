from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'somekey'

@app.route('/')
def index():
    print("normal")
    print (session)
    if 'count' in session:
        session['count']+=1
    else:
        session['count']=1
    return render_template("index.html", count=session['count'])

@app.route('/reset', methods=['POST'])
def reset():
    session['count']=1
    print ("reset")
    print (session)
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)