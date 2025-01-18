from flask import Flask, render_template
import random
import requests
from datetime import date
import time
app = Flask(__name__)


@app.route('/')
def home():
  random_number = random.randint(1, 10)
  year = date.today().year
  return render_template("index.html", num=random_number, year=year)

@app.route('/guess/<string:name>')
def guess(name):
  params = {
    "name": name
  }
  age = requests.get('https://api.agify.io?', params=params)
  return f'Hey {name.capitalize()}\
   You are maybe {age['name']} '


if __name__ == "__name__":
  app.run(debug=True)
