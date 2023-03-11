from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()
    quote = random.choice(quotes).strip()
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
