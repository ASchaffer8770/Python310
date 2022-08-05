from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key="key key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def count():
    if "count" not in session:
        session['count'] = 1
    else: 
        session['count'] += 1
    print(request.form)
    return redirect('/')

@app.route("/destroy_session", methods=['POST'])
def destroy():
    session['count'] = 0
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    