from flask import Flask, render_template
import random
import requests
from datetime import date
import regex
import time
app = Flask(__name__)


@app.route('/')
def home():
  random_number = random.randint(1, 10)
  year = date.today().year
  return render_template("index.html", num=random_number, year=year)

@app.route('/guess/<string:name>')
def get_guess(name):
  params = {
    "name": name
  }
  age = requests.get('https://api.agify.io?', params=params).json()['age']
  url = "https://api.genderapi.io/api/"
  payload = f'name={name}&key=678d450fdfdd22d04ad4507c'
  headers = {
      'Content-Type': 'application/x-www-form-urlencoded'
  } 
  gender = requests.request("POST", url, headers=headers, data=payload).json()['gender']
  
  return render_template('index2.html', gender=gender, age=age, name=name)


@app.route("/blog/<num>")
def get_blog(num):
  print(num)
  blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
  response = requests.get(blog_url)
  all_posts = response.json()
  return render_template("blog.html", posts=all_posts)


if __name__ == "__name__":
  app.run(debug=True)
