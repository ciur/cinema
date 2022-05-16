import random
import time
from flask import jsonify
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


@app.route("/api/items")
def items():
    data = [
        {'item': f"item {random.randrange(1, 15)}"}
        for i in range(15)
    ]
    time.sleep(5 + random.randrange(1, 3))
    return jsonify(data)


if __name__ == '__main__':
    app.run()
