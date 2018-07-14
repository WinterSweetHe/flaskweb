from flask import render_template, redirect, url_for
from flask_login import current_user, login_required

from . import main
from .forms import PostForm
from ..models import Post
from ..email import send_email
from .. import db


@main.route("/", methods=['GET', 'POST'])
@login_required
def index():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(body=form.body.data, author=current_user._get_current_object())
        db.session.add(post)
        return redirect(url_for('main.index'))
    posts = Post.query.order_by(Post.timestamp.desc()).all()
    return render_template("index.html", form=form, posts=posts)


@main.route("/test/sendemail")
def email_test():
    user = {
        "username": "sara"
    }
    send_email("412008380@qq.com", 'New User', 'mail/new_user', user=user)
