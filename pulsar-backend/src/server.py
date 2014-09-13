from flask import Flask

app = Flask(__name__)

@app.route('/register')
def register():
    return 'registering...'

@app.route('/listen')
def listen():
    return 'listening...'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

