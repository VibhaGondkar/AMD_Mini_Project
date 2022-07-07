from flask import Flask,request,Response,make_response,jsonify
import requests

app = Flask(__name__)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return http 500 status code"""
    return make_response(jsonify({'error' : 'Internal Server Error'}), 500)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return http 404 status code"""
    return make_response(jsonify({'error' : 'The requested URL was not found on the server'}), 404)


#api to executeshellscript
@app.route('/executeshellscript', methods=['GET', 'POST', 'PUT'])
def callshellscript():
    try:
        data = request.get_json()
        print(data)

        responce_cvm = requests.get(url= "http://127.0.0.1:5500/cvm-shellscript", params=data )
        responce_svm = requests.get(url= "http://127.0.0.1:5500/svm-shellscript", params=data )

        return Response(status=200)
    except Exception as e:
        return e



#api to list all the folders
@app.route('/listfolderstructure')
def listfolder():

    responce = requests.get(url="http://127.0.0.1:5500/index-listfolder")
    print(responce.json())

    return responce.json()


#api to get the results
@app.route('/getresult')
def res():

    responce = requests.get(url="http://127.0.0.1:5500/index-results")


    return responce.json()


app.run(host='0.0.0.0',port=4000)