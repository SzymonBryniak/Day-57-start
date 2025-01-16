from flask import Flask, render_template
import random
import datetime
app = Flask(__name__)


@app.route('/')
def home():
  random_number = random.randint(1, 10)
  current_year = str(datetime.date.year)
  return render_template("index.html", num=random_number, year=current_year)


if __name__ == "__name__":
  app.run(debug=True)