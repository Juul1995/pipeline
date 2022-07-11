from flask import Flask
import random

app = Flask(__name__)

# Print a random number between 0 and 10
@app.route("/")
def number():
    return random.randint(0, 10)

if __name__ == "__main__":
    app.run()
