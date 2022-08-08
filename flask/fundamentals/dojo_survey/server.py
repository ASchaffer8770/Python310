from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "fruits"
app = Flask(__name__, static_url_path='/static')

@app.route("/")
def survey():
    return render_template("index.html")

@app.route('/results')
def results():
    return render_template("result.html")

if __name__=="__main__":   
    app.run(debug=True)    