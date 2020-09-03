from flask import Flask, jsonify, make_response
from flask import request
from pg_client import execute_query
import json

app = Flask(__name__)


@app.route('/get-test-data/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        query = "SELECT * FROM amazing_report_3 LIMIT 5;"
        records = execute_query(query)
        response = jsonify(records)
        return response



if __name__ == '__main__':
    app.run(host='0.0.0.0', use_reloader=True)
