# MyTodo
step1:<br>
Run 'pip install -r requirements.txt' on terminal

step2: <br>
run in terminal in directory outside main project folder:

export FLASK_APP = MyTodo<br>

export FLASK_DEBUG = 1

step 3 :
run in python interpreter:

from MyTodo import db, create_app, models
<br>
db.create_all(app=create_app())

step 4:
run in terminal in directory outside main project folder:<br>


flask run

step 5:
go to localhost:5000
