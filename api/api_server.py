
#!/usr/bin/env python3
from flask import Flask, jsonify

app = Flask(__name__)

data = {
    "object1": {
        "size": 10,
        "weight": 5,
        "status": "0",
        "quantity": 20
    },
    "object2": {
        "size": 8,
        "weight": 3,
        "status": "1",
        "quantity": 15
    },
    "object3": {
        "size": 12,
        "weight": 7,
        "status": "2",
        "quantity": 25
    }
}

@app.route('/api/objects', methods=['GET'])
def get_objects():
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3003)
