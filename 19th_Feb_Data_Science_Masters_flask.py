from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/hello1")
def hello_world1():
    return "Hello, World 1!"

@app.route("/hello2")
def hello_world2():
    return "Hello, World 2!"

@app.route("/test_func")
def test_func():
    a = 5 + 6
    return f"The sum of two numbers is: {a}"
 

@app.route("/input_url")
def req():
    data = request.args.get("x")
    return f"This is input url for {data}"


if __name__=="__main__":
    app.run(host="0.0.0.0")