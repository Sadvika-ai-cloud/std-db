from flask import Flask,render_template,request
import sqlite3

app=Flask(__name__)
DATABASE=r'c:\sqlite\std.db'
def get_connection():
    cn=sqlite3.connect(DATABASE)
    return cn
@app.route('/')
def index():
    return render_template("std.html")
@app.route('/save',methods=['post'])
def save():
    name=request.form["name"]
    usn=request.form["usn"]
    subjects=request.form["sub"]
    email=request.form["email"]
    connect=get_connection()
    connect.execute("insert into student values(?,?,?,?)",(name,usn,subjects,email))
    connect.commit()
    connect.close()
    return render_template('success.html')
@app.route('/load')
def load():
    connect=get_connection()
    stds=connect.execute("select * from student").fetchall()
    connect.close()
   
    return render_template('load.html',stds=stds)
@app.route('/search',methods=['post'])
def search():
    usn=request.form["usn"]
    connect=get_connection()
    std=connect.execute("select * from student where id=?",(usn,)).fetchone()
    connect.close()
    return render_template('search.html',std=std)
@app.route("/find")
def find():
    return render_template("find.html")
if'__name__'=='__main__':
    app.run(debug=False)