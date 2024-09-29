from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

db = SQLAlchemy()

def create_app():
  app = Flask(__name__, template_folder='templates')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
  db.init_app(app)

  from routes import register_routes
  register_routes(app, db)
  Migrate(app, db)

  return app
  # # part 1: First flask project
  # @app.route('/')
  # def index():
  #   return 'Hello, World!'

  # # part 2: routes
  # @app.route('/user/<string:name>/<int:age>')
  # def userInfo(name, age):
  #   return f'user is {name} age of {age}'

  # @app.route('/greet-user')
  # def greetUser():
  #   greet = request.args.get('greet')
  #   name = request.args.get('name')
  #   return f'{greet}, {name}'

  # #part 3: templates & HTML
  # @app.route('/index')
  # def index_html():
  #   title = "index of page"
  #   return render_template('index.html', title=title)

  # # part 4: Form, Post
  # @app.route('/auth', methods=['GET', 'POST'])
  # def handle_auth():
  #   if request.method == 'GET':
  #     return render_template('auth.html', title="Form")
  #   elif request.method == 'POST':
  #     username = request.form.get('username')
  #     password = request.form.get('password')
  #     return f'username: {username}\npassword: {password}'

  # # part 6: sessions & cookies
  # @app.route('/session-and-cookies')
  # def session_and_cookies():
  #   return render_template('session_cookies.html', message_from_session='No session nor cookies')

  # @app.route('/set-session')
  # def set_session():
  #   session['name'] = 'hilman'
  #   session['role'] = 'user'
  #   session['age'] = 22
  #   return render_template('session_cookies.html', message_from_session='Session set.')

  # @app.route('/get-session')
  # def get_session():
  #   if 'name' in session.keys() and 'role' in session.keys() and 'age' in session.keys():
  #     name = session['name']
  #     role = session['role']
  #     age = session['age']
  #     return render_template('session_cookies.html', message_from_session=f'user: {name} role: {role} age: {age}')
  #   else:
  #     return render_template('session_cookies.html', message_from_session=f'no session found')
      

  # @app.route('/clear-session')
  # def clear_session():
  #   session.clear()
  #   return render_template('session_cookies.html', message_from_session='session cleared')

  # @app.route('/set-cookies')
  # def set_cookies():
  #   response = make_response(render_template('session_cookies.html', message_from_session='cookies set.'))
  #   response.set_cookie('cookie1', 'a cookie')
  #   return response

  # @app.route('/get-cookies')
  # def get_cookies():
  #   cookie = request.cookies['cookie1']
  #   return render_template('session_cookies.html', message_from_session=f'cookie: {cookie}')

