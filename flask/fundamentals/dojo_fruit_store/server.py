from flask import Flask, render_template, request, redirect, session
app = Flask(__name__, static_url_path='/static')
app.secret_key = "fruits"

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    return render_template('checkout.html')
        
@app.route('/order_complete', methods = ['GET'])
def completedOrder():
    print(request.form)
    return render_template('complete.html')

@app.route('/fruits')         
def fruits():
    return render_template("fruits.html",)

if __name__=="__main__":   
    app.run(debug=True)    