from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

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

#part 3: templates & HTML
@app.route('/index')
def index_html():
  title = "index of page"
  return render_template('index.html', title=title)

# part 4: Form, Post
@app.route('/auth', methods=['GET', 'POST'])
def handle_auth():
  if request.method == 'GET':
    return render_template('auth.html', title="Form")
  elif request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    return f'username: {username}\npassword: {password}'


if __name__ == "__main__":
  app.run(host='127.0.0.1', debug=True)