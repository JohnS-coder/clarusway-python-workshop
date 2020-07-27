from flask import Flask,render_template,request,redirect,url_for
import sqlite3

app = Flask(__name__)


con = sqlite3.connect("MYSQLite.db",check_same_thread=False)
cursor = con.cursor()
print("Connected to SQLite")
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS users (name TEXT,email TEXT)")

def find_emails(param):
    cursor.execute("select * from users WHERE name = ?",[param])
    data=cursor.fetchall()
    return data

def insert_email(param1,param2):
    if find_emails(param1):
        print(f"Warning!! {param1} already exists")
    elif param1 and param1.isspace():
        print("Can not be null value")
    else:
        cursor.execute('''INSERT INTO users (name,email) VALUES (?,?);''',(param1,param2))
        con.commit()

@app.route("/")
def home():
    return render_template("index.html",name="John")

@app.route("/add-email",methods=['POST','GET'])
def add_email():
    if request.method== "POST":
        result=0
        email = request.form['useremail']
        name = request.form['username']
        if name and name.isspace():
            name = "Name can not be null value"
            return render_template("index.html",name2=name,show_result=True)
        cursor.execute("select * from users")
        data2=cursor.fetchall()
        for i in data2:
            if i[0]==name:
                name+=" already exist!"
                return render_template("index.html",name2=name,show_result=True)

        cursor.execute('''INSERT INTO users (name,email) VALUES (?,?);''',(name,email))
        con.commit()
        print("Python Variables inserted successfully into users table")
        result =name+" "+email
        if(result):
            return render_template("add-email.html",result=result,show_result=True)
        # return redirect (url_for('add-email.html'), result=result)

    else : 
        return render_template("add-email.html")
        # con.close()
@app.route("/emails.html",methods=['GET','POST'])
def emails():
    cursor.execute("SELECT * from users")
    data=cursor.fetchall()
    if request.method=="POST":
        # name=request.form['username']
        return render_template("emails.html",name_emails=data,show_result=True)
    return render_template("emails.html")
if __name__ == "__main__":
    
    create_table()
    insert_email("ali","ali@gmail.com")
    app.run(debug=True)
    #app.run(host="0.0.0.0",port=80)