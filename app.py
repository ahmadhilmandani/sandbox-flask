from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
  return render_template('index.html', message='Hello World', title='Index')


if __name__ == 'main':
  app.run(host='127.0.0.1', debug=True)