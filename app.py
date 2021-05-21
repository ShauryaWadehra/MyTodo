from flask import Flask, render_template, request, redirect, Blueprint, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from . import db
from .models import Todo

app = Blueprint('app',__name__)

@app.route('/update/<int:sno>', methods=['GET', 'POST'])
def update(sno):
    if request.method=='POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/profile")
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template('update.html', todo=todo)

@app.route('/delete/<int:sno>')
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/profile")

@app.route("/complete/<int:sno>")
def complete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect("/profile")    

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')
@app.route('/termsofuse', methods = ['GET'])
def termsofuse():
    return render_template('termsofuse.html')
@app.route('/privacy', methods = ['GET'])
def privacy():
    return render_template('privacy.html')
    