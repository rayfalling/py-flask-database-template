from flask import render_template, flash, url_for, redirect, session
from application.controller import UserForm, RegisterForm
from application.handler import user as user_handler
from application import app


@app.route("/login", methods=["GET", "POST"])
def login():
    form = UserForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_handler.login(username, password):
            session["login"] = True
            session["username"] = username
            flash('登录成功', category='success')
            return redirect(url_for('index'))
        else:
            flash('用户名或密码错误', category='error')
            form.username = username
            return render_template("login.html", form=form)
    return render_template("login.html", page_title="登录", form=form)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        if user_handler.register_user(username=username, password=password):
            flash('注册成功', category='success')
            form.username = username
            return redirect(url_for('login'))
        else:
            flash('用户已存在', category='success')
            return render_template("register.html", title="注册", form=form)
    return render_template("register.html", page_title="注册", form=form)


@app.route("/logout", methods=["GET", "POST"])
def logout():
    flash('注销成功', category='success')
    session["login"] = False
    session["username"] = ""
    return redirect(url_for("login"))
