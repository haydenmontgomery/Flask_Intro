from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def math_add():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(add(a,b))

@app.route('/sub')
def math_subtract():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(sub(a,b))

@app.route('/mult')
def math_multiply():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(mult(a,b))

@app.route('/div')
def math_divide():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    return str(div(a,b))

#Further Study
@app.route('/math/<operation>')
def operations(operation):
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    if (operation == 'add'):
        return str(add(a,b))
    elif (operation == 'sub'):
        return str(sub(a,b))
    elif (operation == 'mult'):
        return str(mult(a,b))
    else:
        return str(div(a,b))