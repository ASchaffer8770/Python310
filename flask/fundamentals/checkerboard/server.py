from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checker():
    return render_template("index.html")

@app.route('/<int:x>')
def row(x):
    return render_template("single.html", row=x, col=8,color_one='green', color_two='black' )

@app.route('/<int:x>/<int:y>')
def row_col(x,y):
    return render_template("single.html", row=x, col=y, color_one='green', color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>')
def one_tone(x,y,one):
    return render_template('single.html', row=x, col=y, color_one=one, color_two='black')

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def two_tone(x,y,one,two):
    return render_template('single.html', row=x, col=y, color_one=one, color_two=two)

if __name__=="__main__": 
    app.run(debug=True)