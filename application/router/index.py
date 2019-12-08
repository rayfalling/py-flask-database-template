from flask import render_template, flash, url_for, redirect, session
from application.controller import Category
from application.handler import meals as meals_handler
from application import app


@app.route("/")
def root():
    if session.get("login") is True:
        return redirect(url_for("index"))
    return redirect(url_for("login"))


@app.route("/index", methods=["GET", "POST"])
def index():
    form = Category()
    if session.get("login") is True:
        if form.validate_on_submit():
            choice = form.category.data
            rec = meals_handler.query_recommend(category=choice)
            flash("{} 为您推荐: {}".format(choice, rec))
        return render_template("index.html", form=form)
    return redirect(url_for("login"))
