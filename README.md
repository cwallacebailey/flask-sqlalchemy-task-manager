pip3 install Flask-SQLAlchemy psycopg2

# type psql, then enter, then CREATE DATABASE taskmanager; then \c taskmanager and the below will show. 

gitpod /workspace/flask-sqlalchemy-task-manager $ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# CREATE DATABASE taskmanager;
CREATE DATABASE
postgres=# \c taskmanager;
You are now connected to database "taskmanager" as user "gitpod".
taskmanager=# 

# hit \q to leave and now we connect the database
# type python3 
# type from taskmanager import db
# type db.create_all()











import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "any_secret_key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("DB_URL", "postgresql:///taskmanager")