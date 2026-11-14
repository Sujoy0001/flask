from flask import Flask
from uuid import UUID

app = Flask(__name__)

@app.route("/")
def root():
   return "hello world"

@app.route("/about")
def about():
    return "about page"

@app.route("/user")
def user():
    return "user page"

@app.route('/user/<name>')
def userabout(name):
    return f" hello {name} is it your page?"

@app.route('/student/<course>/<name>')
def student(course,name):
    return f" hello {name}. your course is {course}."

@app.route("/price/<float:number>")
def productPrice(number):
    return f"this product is {number} $"

@app.route("/root/<uuid:user_id>")
def root_id(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)