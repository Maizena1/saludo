from flask import Flask
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "El leo es un pendejo jajajajajajaja pendejo"
 
if __name__ == "__main__":
    app.run()
