from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world2():
    return "Hello World2"

@app.route ('/dojo')
def dojo():
    return "Dojo!"

@app.route ('/say/<name>')
def name(name):
    return f"Hi " + name

@app.route ('/say/<int:num>/<string:word>')
def multi_name(num, word):
    output = ''
    for i in range(0,num):
        output += f"<p>{word}</p>"
    return output

if __name__=="__main__": 
    app.run(debug=True)