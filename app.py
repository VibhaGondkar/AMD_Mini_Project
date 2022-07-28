from flask import Flask,request,Response,make_response,jsonify
import requests
import os
# import paths_and_url
from config import CVM_URL, SVM_URL
# from .amd_app.demo import base_url
app = Flask(__name__)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return http 500 status code"""
    return make_response(jsonify({'error' : 'Internal Server Error'}),500)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return http 404 status code"""
    return make_response(jsonify({'error' : 'The requested URL was not found on the server'}),404)

@app.route('/executeshellscript')
def callshellscript():
    try:
        data = request.get_json()
        print(data)

        responce_cvm = requests.get(url= CVM_URL + "cvm-shellscript", params=data )
        responce_svm = requests.get(url= SVM_URL + "svm-shellscript", params=data )

        return Response(status=200)
    except Exception as e:
        return e




@app.route('/listfolderstructure')
def listfolder():

    responce = requests.get(url="http://127.0.0.1:5500/index-listfolder")
    print(responce.json())

    return responce.json()



@app.route('/getresult')
def res():

    responce = requests.get(url= BASE_URL + "index-results")


    return responce.json()

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=4000)