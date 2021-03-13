Kyle Davis -- kdavis18 -- QP45770

Individual Assignment

This app will allow you to run a web server connected to a local 
SQLITE database and store the names, school ids, and grades of students.
You are able to create new students, update existing ones, delete
them, or simply read those which have been stored.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

Dependencies:
Flask
SQLAlchemy
Flask-SQLAlchemy

You should be able to get away with simply running the following 
command in a virtual environment:

pip3 install flask sqlalchemy flask-sqlalchemy

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

Note about database:
Since the database layer is written in SQLite, the database is stored
in a local file. I have included the file, studentdata.db, which is
the database file I used in the creation of this app. If, for some
reason, the app won't work with the downloaded db file or you
wish to use your own, you can initialize the database with the
following commands in a python3 terminal:

>>> from bookmanager import db
>>> db.create_all()
>>> exit()

This will initialize a new studentdata.db file.

-------------------------------------------------------------------------------
-------------------------------------------------------------------------------

To run the application, simply run the studentmanager.py file, which
will launch the web server on the local host (http://127.0.0.1:5000/).
Open up the page in a browser, and you should be good to use all
of the applications features.