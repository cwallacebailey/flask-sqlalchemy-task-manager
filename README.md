pip3 install Flask-SQLAlchemy psycopg2

gitpod /workspace/flask-sqlalchemy-task-manager $ psql
psql (12.9 (Ubuntu 12.9-0ubuntu0.20.04.1))
Type "help" for help.

postgres=# CREATE DATABASE taskmanager;
CREATE DATABASE
postgres=# \c taskmanager;
You are now connected to database "taskmanager" as user "gitpod".
taskmanager=# 