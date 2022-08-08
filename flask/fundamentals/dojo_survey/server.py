from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "this is a survey"

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def survey():
    return render_template("index.html")

@app.route("/submit", methods = ["POST"])
def submit():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/results')

@app.route('/results')
def results():
    return render_template("result.html", name = session['name'], location = session['location'], language = session ['language'],
    comments = session['comments'])

if __name__=="__main__":   
    app.run(debug=True)    