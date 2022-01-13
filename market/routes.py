from market import app
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm
from market import db
from flask_login import login_user, logout_user, login_required


@app.route('/')
@app.route('/home_page')
def home_page():
    return render_template('home.html')

@app.route('/market_page')
@login_required
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