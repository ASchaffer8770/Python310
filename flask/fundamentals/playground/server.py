from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def home():
    num = 3
    color = "aqua"
    return render_template('index.html', num=num, color=color)

@app.route('/play/<int:num>')
def two(num):
    return render_template('index.html', num=num)

@app.route('/play/<int:num>/<color>')
def three(num, color):
    return render_template('index.html', num = num, color = color)


if __name__=="__main__":
    app.run(debug=True)