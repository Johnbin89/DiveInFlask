from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, current_app
from . import main
from ..import db
from .. import mysql
from ..models import Divespot
from ..email import send_email
from .forms import NameForm

from sqlalchemy import func

@main.route('/', methods=['GET', 'POST'])
def index():
    '''
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username = form.name.data)
            db.session.add(user)
            session['known'] = False
            if current_app.config['FLASKY_ADMIN']:
                send_email(current_app.config['FLASKY_ADMIN'], 'New User', 'mail/new_user', user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('.index'))
    '''
    random_spots = Divespot.query.order_by(func.random()).limit(3).all()
    print(random_spots)
    #return render_template('index.html', form=form, name=session.get('name'), known = session.get('known', False), current_time=datetime.utcnow())
    return render_template('index.html', random_spots=random_spots)

@main.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@main.route('/services')
def services():
    return render_template('services.html')

@main.route('/contactus')
def contactus():
    return render_template('contactus.html')