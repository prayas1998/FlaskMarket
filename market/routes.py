from flask_login import login_user

from market import app, db
from flask import render_template, redirect, url_for, flash
from market.models import Item, User
from market.forms import RegisterForm, LoginForm


@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/about")
def about_page():
    return "<h1>This is about page</h1>"


@app.route("/market")
def market_page():
    items = Item.query.all()
    return render_template('market.html', items=items)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)   # https://www.notion.so/FlaskMarket-First-Project-e2d9190761314c40a4f4f2652b12b21a?pvs=4#79af22a2c2cf49b9b4d5eed149cb8b44
        db.session.add(user_to_create)
        db.session.commit()
        return redirect(url_for('market_page'))

    if form.errors != {}:  # If there are no errors from the validations
        for err_msg in form.errors.values():
            # print(f'There was an error with creating a user: {err_msg}') # This prints message on server side i.e terminal
            flash(f'There was an error with creating a user: {err_msg}',
                  category='danger')  # This flashes error message to user
    return render_template('register.html', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    attempted_user = User.query.get(form.username.data).first()
    if attempted_user and attempted_user.check_password_correction(attempted_password='form.password.data'):
        login_user(attempted_user)
        flash(f'Success! You are now logged in as {attempted_user}', category='success')
        return redirect(url_for('market_page'))

    else:
        flash('Username and passwords do not match. Please try again!', category='danger')

    return render_template('login.html', form=form)
