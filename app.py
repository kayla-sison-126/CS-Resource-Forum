from flask import Flask
from routes.submit import submit_blueprint

app = Flask(__name__)
app.register_blueprint(submit_blueprint)

@app.route('/')
def home():
    return "Hello from Flask! :)"

if __name__ == '__main__':
    app.run(debug=True)
