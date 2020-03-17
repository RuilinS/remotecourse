# _*_coding:utf-8_*_
from flask import Flask
from flask import request,jsonify
import os
import time
import warnings
from get_digit_info import Solver, Net
#from op import OP
warnings.filterwarnings("ignore")

app = Flask(__name__)

# 加载模型
solver = Solver()
solver.load_model()
use_db = False

if use_db:
    print('load db')
    #op_h = OP()
    #op_h.init_op()

@app.route('/ocr', methods=['POST'])
def upload():
    result = {}
    result["status_code"] = "200"
    result["status_info"] = "sucess"
    result["digit"] = "-1"
    try:
        f = request.files['file']
        # 当前文件所在路径
        basepath = os.path.dirname(__file__)
        # 缓存路径
        upload_path = os.path.join(basepath, 'images')
        if os.path.exists(upload_path) is False:
            os.makedirs(upload_path)
        tn = time.time()
        fi = os.path.join(upload_path, str(int(round(tn * 1000000))) + '.jpg')
        f.save(fi)
        # 识别图片
        digit = solver.run_single(fi)
        result["digit"] = str(digit)
        if use_db:
            # 保存图片
            try:
                print('save to db')
                #op_h.save_image(fi)
            except:
                pass
        os.remove(fi)
    except Exception as e:
        print("Error: ", e)
        result["status_code"] = "500"
        result['status_info'] = str(e)

    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=False, threaded=True)