from flask import Flask, request

app = Flask(__name__)

# part 1: First flask project
@app.route('/')
def index():
  return 'Hello, World!'

# part 2: routes
@app.route('/user/<string:name>/<int:age>')
def userInfo(name, age):
  return f'user is {name} age of {age}'

@app.route('/greet-user')
def greetUser():
  greet = request.args.get('greet')
  name = request.args.get('name')
  return f'{greet}, {name}'
if __name__ == "__main__":
  app.run(host='127.0.0.1', debug=True)