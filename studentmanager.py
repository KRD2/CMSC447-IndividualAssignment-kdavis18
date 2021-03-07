import os

from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy

############################################################################################################

project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "studentdata.db"))

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Student(db.Model):
    first_name = db.Column(db.String(20), unique=False, nullable=False, primary_key=False)
    school_id = db.Column(db.String(2), unique=True, nullable=False, primary_key=True)
    grade = db.Column(db.String(3), unique=False, nullable=False, primary_key=False)

    def __repr__(self):
            return "<Name: {}\tID: {}\tMarks: {}>".format(self.first_name, self.school_id, self.grade)

############################################################################################################

@app.route("/", methods=["GET","POST"])
def main():
    if request.form:
        student = Student(first_name=request.form.get("first_name"),
                          school_id=request.form.get("id"),
                          grade=request.form.get("grade"))
        db.session.add(student)
        db.session.commit()
    students = Student.query.all()
    return render_template("main.html", students=students)

############################################################################################################

@app.route("/update", methods=["POST"])
def update():
    newname = request.form.get("newname")
    newid = request.form.get("newid")
    oldid = request.form.get("oldid")
    newgrade = request.form.get("newgrade")
    student = Student.query.filter_by(school_id=oldid).first()
    student.first_name = newname
    student.school_id = newid
    student.grade = newgrade
    db.session.commit()
    return redirect("/")

############################################################################################################

@app.route("/delete", methods=["POST"])
def delete():
    id = request.form.get("id")
    student = Student.query.filter_by(school_id=id).first()
    db.session.delete(student)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run()