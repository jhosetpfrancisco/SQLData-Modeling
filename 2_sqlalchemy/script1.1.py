from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "<p>Hola Mundo!</p>"


if __name__ == '__main__':
    app.debug = True  # Only for debug
    app.run(host="0.0.0.0", port=5001)
