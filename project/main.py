# main.py

from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from .models import Todo
from . import db
main = Blueprint('main', __name__)

@main.route('/', methods = ['GET','POST'])
def index():
    return render_template('index.html')

@main.route('/profile', methods = ['GET','POST'])
@login_required
def profile():
    if request.method == 'POST':
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
        
    allTodo = Todo.query.all() 
    return render_template('profile.html', allTodo=allTodo, name = current_user.name)    