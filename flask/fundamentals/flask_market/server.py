from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home') #directs to home page. both routes point to index.html
def hello_world2():
    return render_template('index.html')

@app.route('/market')
def market_page():
    inventory = [
        {'id': 1, 'name': 'Phone', 'barcode': '893212299897', 'price': 500},
        {'id': 2, 'name': 'Laptop', 'barcode': '123985473165', 'price': 900},
        {'id': 3, 'name': 'Keyboard', 'barcode': '231985128446', 'price': 150}
    ]
    return render_template('market.html', items = inventory)

# @app.route('/about/<username>') #this is dymanic routing!!
# def about_page(username):
#     return f'This the About page of {username}'

if __name__=="__main__": 
    app.run(debug=True)