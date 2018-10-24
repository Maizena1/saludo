from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Fuga a las 6:00 p.m."
 
if __name__ == "__main__":
    app.run()
