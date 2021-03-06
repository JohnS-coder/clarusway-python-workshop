from flask import Flask,redirect,url_for,render_template,send_file

app = Flask(__name__)#static_url_path="/C://Users\Ahmet\coder-git\clarusway-python-workshop\flask-02-handling-routes-and-templates-on-ec2-linux2\static\mytext.txt")


@app.route("/")
def home():
    return "This is home page!..for no path, <h1>Welcome Home</h1> "

@app.route("/about")
def about():
    return '<h1>This is my about page </h1>' 
@app.route("/static")
def stat():
    return send_file("C:/Users/Ahmet/coder-git/clarusway-python-workshop/flask-02-handling-routes-and-templates-on-ec2-linux2/static/mytext.txt",attachment_filename="mytext.txt")
# @app.route("/about")
# def about():
#     return '<h1>Either you encountered an error or you are not authorized.</h1>'

@app.route("/hello")
def hello():
    return "<h1>HELLO WORLD</h1>"

@app.route("/error")
def error():
    return "<h1>You don't have permission to display this page..</h1>"

@app.route("/admin")
def admin():
    return redirect(url_for("error"))



# @app.route('/<name>')
# def greet(name):
#     greet_format = f"""
# <!DOCTYPE html>
# <html>
# <head>
#     <title>Greeting Page</title>
# </head>
# <body>
#     <h1>Hello, { name }!</h1>
#     <h1>Welcome to my Greeting Page</h1>
# </body>
# </html> 
#     """
#     return greet_format

@app.route("/greet-admin")
def greet_admin():
    return render_template("greet.html",name="Great admin MASTER!!.")

@app.route("/<username>")
def greet(username):
    return render_template("greet.html",name=username)

@app.route("/list10")
def list10():
    return render_template("list10.html")

@app.route("/evens")
def evens():
    return render_template("evens.html")

if __name__ == "__main__":
    app.run(debug=True)