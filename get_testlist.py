from flask import Flask, request, Response, make_response, jsonify
import requests
import collections
# import json

app = Flask(__name__)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return http 500 status code"""
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return http 404 status code"""
    return make_response(jsonify({'error': 'The requested URL was not found on the server'}), 404)


# @app.route('/get_testlist')
# def testlist():
#     response = requests.get(url="http://127.0.0.1:5500//get_list")
#     response1 = response.json()
#     print(response1)
#     return 'ok'

# @app.route('/get_testlist')
# def testlist():
#     response = requests.get(url="http://127.0.0.1:5500//get_list")
#     response1 = response.json()
#
#     svm = response1[0]
#     cvm = response1[1]
#     result = []
#     # traverse through svm and cvm keys to find similar files
#     for i in svm:
#         for k in cvm:
#             for j in i.keys():
#                 if j in k.keys():
#                     svm_value = i[j]
#                     cvm_value = k[j]
#                     result.append({j: [svm_value, cvm_value]})
#                 # else:
#                 #     return jsonify({"error": "test failed!!"})
#
#         # result.append(resp)
#     return jsonify(result)

@app.route('/get_testlist')
def testlist():
    response = requests.get(url="http://127.0.0.1:5500//get_list")
    response1 = response.json()

    svm = response1[0]
    cvm = response1[1]
    result = []
    list1 = []
    list2 = []
    for i in svm:
        for j in i.keys():
            list1.append(j)
    for i in cvm:
        for j in i.keys():
            list2.append(j)
    if collections.Counter(list1) == collections.Counter(list2):
        for i in svm:
            for k in cvm:
                for j in i.keys():
                    if j in k.keys():
                        svm_value = i[j]
                        cvm_value = k[j]
                        result.append({j: [svm_value, cvm_value]})
        return jsonify(result)
    else:
        return jsonify({"error": "test failed!"})



app.run(host='0.0.0.0', port=4000, debug=True)
