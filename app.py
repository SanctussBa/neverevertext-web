from flask import Flask, render_template, url_for
import random


app = Flask (__name__)

@app.route('/')
def welcome():
    return render_template('home.html')

@app.route('/game')
def game():
    from bla import list_oftext
    number = random.randint(0,60)
    line = list_oftext[number]
    return render_template('start.html', line = line)


if __name__ == '__main__':
    app.run(debug=True)
