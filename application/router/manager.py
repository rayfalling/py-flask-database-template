from flask import render_template, flash, url_for, redirect, session, request
from application.handler import meals as meals_handler
from application import app


@app.route("/manager/list")
def manager_list():
    if session.get("login") is True:
        query = meals_handler.query_all()
        return render_template("list.html", list=query)
    return redirect(url_for("login"))


@app.route("/manager/remove")
def manager_remove():
    category = request.args.get('category')
    name = request.args.get('name')
    if session.get("login") is True:
        if meals_handler.delete_item(category, name):
            flash("删除成功")
        return redirect(url_for("manager_list"))
    return redirect(url_for("login"))


@app.route("/manager/name/update", methods=["GET", "POST"])
def manager_update_name():
    if request.method == "POST":
        category_new = request.form.get('category_new')
        category = request.form.get('category')
        name_new = request.form.get('name_new')
        name = request.form.get('name')
        if session.get("login") is True:
            if meals_handler.update_item(category, name, category_new, name_new):
                flash("更新成功")
            return redirect(url_for("manager_list"))
    return redirect(url_for("login"))


@app.route("/manager/add", methods=["GET", "POST"])
def manager_add_item():
    if request.method == "POST":
        category = request.form.get('category')
        name = request.form.get('name')
        if session.get("login") is True:
            if meals_handler.add_item(category, name):
                flash("添加成功")
            return redirect(url_for("manager_list"))
    return redirect(url_for("login"))


__all__ = ["manager_remove", "manager_update_name", "manager_add_item", "manager_list"]
