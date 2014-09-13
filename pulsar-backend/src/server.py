from flask import Flask, request

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
       print request.data

@app.route('/listen')
def listen():
    # hit /SendRequest
    # respone key ispOutage
    return 'listening...'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

