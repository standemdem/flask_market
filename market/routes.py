from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')

@app.route('/market_page')
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)

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
        return redirect(url_for('market_page'))

    # checks if there arer errors when submitting
    if form.errors != {}:
        for err_msge in form.errors.values():
            flash(f'There was an error when creating a user{err_msge}')
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    print('-----------------------test')
    if form.validate_on_submit():
        print('isit HERE ???????????????')
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(attempted_password=form.password.data):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            print('-----------------------test')
            return redirect(url_for('market_page'))
        else:
            print('-----------------------test')
            flash('Username and password are not matched! Please try again', category='danger')

    return render_template('login.html', form=form)
