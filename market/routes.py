from flask import render_template
from market import app
from market.models import Item

@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')

@app.route('/market_page')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)