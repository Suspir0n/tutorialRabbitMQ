from worker_a import add_nums
from worker_b import sub_nums
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/add', methods=['POST'])
def add():
    _json = request.get_json()
    first_num = _json['first_num']
    second_num = _json['second_num']
    result = add_nums.AsyncResult(first_num, second_num)
    return jsonify({'result': result, 'status': result.status}), 200


@app.route('/sub', methods=['POST'])
def sub():
    _json = request.get_json()
    first_num = _json['first_num']
    second_num = _json['second_num']
    result = sub_nums.delay(first_num, second_num)
    return jsonify({'result': result.result(task_id=result.task_id), 'status': result.status}), 200

