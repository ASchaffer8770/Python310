from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world2():
    return render_template('index.html')

@app.route('/about/<username>') #this is dymanic routing!!
def about_page(username):
    return f'This the About page of {username}'

if __name__=="__main__": 
    app.run(debug=True)