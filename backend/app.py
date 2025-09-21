from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "AI Roast Battle Simulator Backend"

if __name__ == "__main__":
    app.run(debug=True)