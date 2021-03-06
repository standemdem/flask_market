from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm,SellItemForm
from market import db
from flask_login import login_user, logout_user, login_required, current_user


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')

@app.route('/market_page', methods=['POST', 'GET'])
@login_required
def market_page():
    items = Item.query.all()
    purchase_form = PurchaseItemForm()
    sell_form = SellItemForm()
    
    if request.method == 'POST':
        # PURCHASE ITEM LOGIC
        purchased_item = request.form.get('purchased_item')
        p_item_object= Item.query.filter_by(name=purchased_item).first()
        if p_item_object:
            if current_user.can_purchase(p_item_object):
                p_item_object.buy(current_user)
                flash(f"Congrats! You've just purchased {p_item_object.name} for {p_item_object.price}", category="success")
            else:
                flash(f"You don't have enough money to buy {p_item_object.name}", category="warning")
        
        # SELL ITEM LOGIC
        sold_item = request.form.get('sold_item')
        s_item_object = Item.query.filter_by(name=sold_item).first()
        if s_item_object:
            if current_user.can_sell(s_item_object):
                s_item_object.sell(current_user)
                flash(f"Congrats! You've just sold {s_item_object.name} for {s_item_object.price}", category="success")
            else:
                flash(f"somethig wen't wrong with {s_item_object.name}", category="danger")
        
        return redirect(url_for('market_page'))
    
    if request.method == 'GET':
        # If you want to display only available items in stock
        # items= Item.query.filter_by(owner= None)
        # If you want to display the whole db
        items = Item.query.all()
        
        owned_items = Item.query.filter_by(owner = current_user.id)
        return render_template('market.html', items=items, purchase_form=purchase_form, 
                                sell_form=sell_form, owned_items=owned_items)

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    # creates a new user and import it to db on submit
    if form.validate_on_submit():
        user_to_create = User(username = form.username.data,
                                email = form.email.data,
                                password = form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f'You\'ve successfully created your account! You are now logged in as {user_to_create.username}', category="success")
        return redirect(url_for('market_page'))

    # checks if there are errors when submitting
    if form.errors != {}:
        for err_msge in form.errors.values():
            flash(f'There was an error when creating a user{err_msge}')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', 'success')
            print(f'{attempted_user.username} has logged in')
            return redirect(url_for('market_page'))
        else:
            print('wrong login or password')
            flash('Username and password are not matched! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash(f"You have been successfully logged out", 'info')
    return redirect(url_for('home_page'))