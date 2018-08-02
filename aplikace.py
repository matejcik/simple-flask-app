from flask import Flask, abort, redirect
from flask import render_template
from flask import request
from flask import session
app = Flask("ahoj")
app.secret_key = b"muj tajny klic"

@app.route("/")
def index():
    return "hello"

POCITADLO = 0

VZKAZY = []

@app.route(
    "/vzkazy",
    methods=["GET", "POST"],
)
def vzkazy():
    global VZKAZY
    if "jmeno" in session:
        jmeno = session["jmeno"]
    else:
        jmeno = ""
        session["jmeno"] = ""

    if request.method == "GET":
        return render_template(
            "vzkazy.html",
            vzkazy=VZKAZY,
            jmeno=jmeno,
        )
    else:
        jmeno = request.form["jmeno"]
        session["jmeno"] = jmeno
        vzkaz = request.form["vzkaz"]
        text = jmeno + ": " + vzkaz
        VZKAZY.append(text)
        return redirect("/vzkazy")

@app.route("/poc")
def pocitadlo():
    global POCITADLO
    POCITADLO += 1
    return render_template(
        "poc.html",
        kolik=POCITADLO,
    )

@app.route("/hello/<name>")
def hello(name):
    if name == "karel":
        abort(404)
    elif name == "poc":
        return redirect("/poc")

    return render_template(
        "hello.html",
        name=name,
        myname="matejcik",
    )
