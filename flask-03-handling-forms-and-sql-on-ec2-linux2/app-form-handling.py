from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html",name="John")

# @app.route("/<name>",methods=["Get"])
# def greet(name):
#     return render_template("greet.html",user=name)

@app.route("/greet",methods=["GET"])
def greet():
    if "user" in request.args:
        usr=request.args["user"]
        return render_template("greet.html",user=usr)
    else:
        return render_template("greet.html",user="Send your user name in query string with 'user' ")


@app.route("/loign",methods=["GET","POST"])
def login():
    if request.method == "POST":
        user_name=request.form["username"]
        return render_template("secure.html", user_name)
    else:
        return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host="0.0.0.0",port=80)