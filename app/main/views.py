from flask import render_template, redirect, url_for, session
from datetime import datetime

from . import main
from .forms import NameForm
from .. import db
from ..models import User


@main.route("/", methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if not user:
            user = User(username=form.name.data)
            db.session.add(user)
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('main.index'))
    return render_template("index.html",
                           form=form,
                           name=session.get('name'),
                           known=session.get('known', False),
                           current_time=datetime.utcnow())


@main.route("/user/<name>")
def user(name):
    return render_template("user.html", name=name)
