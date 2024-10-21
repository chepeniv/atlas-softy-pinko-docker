#!/etc/bin/python3
"""
this py script uses flask to output a message

by hosting flask on 0.0.0.0 rather than 127.0.0.1 means that
flask will be reachable outside of the current container
"""

from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/hello')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5252)
