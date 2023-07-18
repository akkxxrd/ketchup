from flask import Flask

# Create an instance of the Flask application
app = Flask(__name__)

# Define a route and its corresponding handler
@app.route('/')
def hello():
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    app.run()

