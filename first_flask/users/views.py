import os
import json
from markupsafe import escape
from flask import Blueprint, render_template, jsonify, request, redirect, url_for

users = Blueprint('users', __name__, url_prefix='/user_info', template_folder=r'D:\first_application\templates')
a = os.getcwd()

data = json.load(open(r'D:\first_application\first_flask\users\data.json', 'r'))
data1 = json.load(open(r'D:\first_application\first_flask\users\data1.json', 'r'))


@users.route('/', methods=['GET'])
def hello():
    print(a)
    # return '<h1>hello world</h1>'
    return jsonify(data)


@users.route('/hello/<name>', methods=['GET'])
def about(name):
    return f'<h1>{escape(name.capitalize())}</h1>'


# @users.route('/welcome')
# def welcome():
#     return render_template("home.html")


@users.route('/<id>/', methods=['GET'])
def show(id):
    response = [x for x in data if x['user_id'] == int(id)]
    return jsonify(response)


@users.route('/query_example', methods=['GET'])
def query_example():
    user_data = request.args.get('user_id')
    new_user = [x for x in data if x['user_id'] == int(user_data)]
    new_user = new_user[0] if new_user else {}
    return jsonify(new_user)


# ----------------------------------------------------------------------------------------------------------------------
# using query arguments
# ----------------------------------------------------------------------------------------------------------------------

# @users.route('/query_example', methods=['GET'])
# def query_example():
#     language = request.args.get('language')
#     framework = request.args.get('framework')
#     return f'language is : {language}\n' \
#            f'framework is : {framework}'
# # http://127.0.0.1:5000/user_info/query_example?language=python  ---> for single query string parameter
# # http://127.0.0.1:5000/user_info/query_example?language=python&framework=flask  ---> for multiple query string paramtrs

# ----------------------------------------------------------------------------------------------------------------------
# using form data
# ----------------------------------------------------------------------------------------------------------------------

# @users.route('/form_example', methods=['POST', 'GET'])
# def form_example():
#     if request.method == 'POST':
#         name = request.form.get('name')
#         password = request.form.get('password')
#         return redirect(url_for('users.show_user', name=name, password=password))
#     else:
#         return render_template('user.html')
#         # return '<h1> hii </h1>'
#
#
# @users.route('/show_user')
# def show_user():
#     store = request.args.get("name")
#     store1 = request.args.get("password")
#     return f'{store} {store1}'

# ----------------------------------------------------------------------------------------------------------------------
# using json data
# ----------------------------------------------------------------------------------------------------------------------


@users.route('/create_user', methods=['POST'])
def create_user1():
    request_data = request.get_json()
    new_user_id = int(data[-1]['user_id']) + 1
    response = request_data
    response['user_id'] = new_user_id
    # response['patil'] = "rohit"
    data.append(response)
    json.dump(data, open(r'D:\first_application\first_flask\users\data.json', 'w'))
    return jsonify(response)


# @users.route('/get_data', methods=['GET'])
# def get_data():
#     req_data = request.get_json()
#     name = req_data[0]['name']
#     course = req_data[1]['course']
#     return jsonify({'name': name, 'course': course})

@users.route('/create_user_form', methods=['POST'])
def create_user2():
    name = request.form.get('name')
    password = request.form.get('password')
    new_user_id = int(data1[-1]['id']) + 1
    response = {
        'id': new_user_id,
        'name': name,
        'password': password
    }
    data1.append(response)
    json.dump(data1, open(r'D:\first_application\first_flask\users\data1.json', 'w'))
    return jsonify(response)


# @users.route('/update_user/<user_id>/', methods=['PUT'])
# def update_user(user_id):
#     request_data = request.get_json()
#     for d in data:
#         if d['id'] == int(user_id):
#             if 'name' in request_data:
#                 d['name'] = request_data['name']
#             if 'password' in request_data:
#                 d['password'] = request_data['password']
#     json.dump(data, open(r'D:\first_application\first_flask\users\data.json', 'w'))
#     return 'User details update successfully'

@users.route('/delete_user/<user_id>/', methods=['DELETE'])
def delete_user(user_id):
    for index, d in enumerate(data):
        if d['user_id'] == int(user_id):
            # del data[index]    # delete whole record related to index
            del data[index]['name']     # delete particular field of record related to index
    json.dump(data, open(r'D:\first_application\first_flask\users\data.json', 'w'))
    return 'User has been deleted successfully'
