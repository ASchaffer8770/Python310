from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "fruits"
app = Flask(__name__, static_url_path='/static')

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    return render_template('checkout.html')

@app.route('/order_complete')
def completedOrder():
    return render_template('complete.html')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html",)

if __name__=="__main__":   
    app.run(debug=True)    