from flask import Flask, request, Response
import json
import pdb

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        payload = request.form
        return Response(response=json.dumps({}), status=200)         

@app.route('/listen')
def listen():
    # hit /SendRequest
    # respone key ispOutage
    return 'listening...'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

