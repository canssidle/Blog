from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from flask_login import login_required,current_user
from ..models import User,Blog,Comment,Subscribe
from .forms import UpdateProfile,BlogForm,CommentForm,SubscribeForm
from .. import db,photos



@main.route('/')
def index():
    mystory =Blog.query.all()
    Comment = Comment.query.all()
    title = "MY PERSINAL BLOG"

    return render_template("index.html,mystory = mystory,comment = comment,title = title")


@app.route("/about.html")
def about():
    return render_template("about.html")

@app.route("/post")
def post():
    return render_template("post.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == '__main__':
