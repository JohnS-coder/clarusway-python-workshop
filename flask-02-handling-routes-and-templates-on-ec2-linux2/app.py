from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "This is home page!.., <h1>HELLO WORLD</h1> "
@app.route("/hello")
def hello():
    return "<h1>HELLO WORLD</h1>"

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
    return redirect(url_for("greet",name="Great admin MASTER!!."))

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