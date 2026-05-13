from flask import Flask, render_template
from flask import request, redirect
from flask import session

app = Flask(__name__)

app.secret_key = "secret123"

@app.route("/", methods=["GET", "POST"])
def login():

    message = ""

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        if username == "admin" and password == "1234":

            session["user"] = username

            return redirect("/dashboard")

        else:
            message = "Wrong information!"

    return render_template(
        "index.html",
        message=message
    )

@app.route("/dashboard")
def dashboard():

    if "user" in session:

        return render_template(
            "dashboard.html",
            user=session["user"]
        )

    return redirect("/")

@app.route("/logout")
def logout():

    session.pop("user", None)

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
