from flask import Flask,request,make_response
import json

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World this is flask!"

@app.route("/hello", methods=['POST'])
def hello1():
    return "i am from hellow"

@app.route("/json")
def servejson():
    list=["josphen", "23232",True,False]
    return json.dumps(list)
@app.route("/json1")
def json1():
    list ={"name":"Tarkeshwar","phone":323232}
    response = make_response(json.dumps(list)) # Set correct mimetype
    response.mimetype = "application/json"
    return response

@app.route("/root/hell/test/test")
def root():
    return "Request Path is: " + request.path

@app.route("/test")
def test():
    return "Request Path is " + request.path

@app.route("/sayhello/<person_name>")
def sayHello(person_name):
    return "Hello Friends - "+person_name

if __name__=="__main__":
    app.run(debug=True)
