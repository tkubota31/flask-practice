# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)


@app.route('/add')
def add_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = add(a,b)
    return str(result)


@app.route('/sub')
def sub_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = sub(a,b)
    return str(result)

@app.route('/mult')
def mult_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = mult(a,b)
    return str(result)

@app.route('/div')
def div_nums():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    result = div(a,b)
    return str(result)


operators = {
    "add" : add,
    "sub" : sub,
    "mult": mult,
    "div" : div,
}

@app.route("/math/<operation>")
def operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    answer = operators[operation](a,b)
    return str(answer)
