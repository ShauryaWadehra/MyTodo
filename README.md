# MyTodo
step1:<br>

run in terminal in directory outside main project folder:

export FLASK_APP = MyTodo<br>

export FLASK_DEBUG = 1

step 2 :
run in python interpreter:

from MyTodo import db, create_app, models
<br>
db.create_all(app=create_app())

step 3:
run in terminal in directory outside main project folder:<br>


flask run

step 4:
go to localhost:5000
