# _*_coding:utf-8_*_
from flask import Flask
from flask import request, jsonify
import os
import time
import warnings

warnings.filterwarnings("ignore")
app = Flask(__name__)


@app.route('/ocr', methods=['POST'])
def upload():
    result = {}
    result["status_code"] = "200"
    result["status_info"] = "sucess"
    result["digit"] = "-1"
    current_path = os.path.dirname(__file__)
    result["current_path"] = current_path


    try:
        lines = []

        with open('info.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
            result["lines1"] = lines

        with open(current_path + '/info.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()

        result["digit"] = lines

    except Exception as e:
        print("Error: ", e)
        result["status_code"] = "500"
        result['status_info'] = str(e)
        return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False, threaded=True)