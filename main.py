from flask import Flask,request,Response
import requests,os,pandas as pd, pathlib
import subprocess

#defining cvm folder path

path_cvm = 'demo/cvm'
path_svm = 'demo/svm'

#function to execute shell script
def MonteCarlo(data):
    TestName = data["TestName"]
    nThreads = data["nThreads"]
    nOptions = data["nOptions"]
    Path_Lenghth = data["Path_Lenghth"]
    test_block_length = data["test_block_length"]

    subprocess.call(['bash','start_test.sh',str(nThreads),str(nOptions),str(Path_Lenghth),str(test_block_length)])
    return



app = Flask(__name__)

@app.route('/cvm-shellscript')
def cvm():

    print("cvm run...")
    #getting data
    args = request.args.to_dict()
    print(args)

    #calling shell script
    MonteCarlo(args)

    return args

@app.route('/svm-shellscript')
def svm():
    print("svm run...")
    #getting data
    args = request.args.to_dict()
    print(args)

    #calling shell script
    MonteCarlo(args)

    return args

@app.route('/index-listfolder')
def list():
    li_dir_cvm = []
    li_files_cvm_test1 = []
    li_files_cvm_test2 = []

    li_dir_svm = []
    li_files_svm_test1 = []
    li_files_svm_test2 = []

    #############svm

    for (root, dirs, file) in os.walk(path_svm):
        for dir in dirs:
            li_dir_svm.append(dir)


    for (root, dirs, file) in os.walk(path_svm + '/' + li_dir_svm[0]):
        for f in file:
            li_files_svm_test1.append(f)

    for (root, dirs, file) in os.walk(path_svm + '/' + li_dir_svm[1]):
        for f in file:
            li_files_svm_test2.append(f)

    dict_svm = {"test1": li_files_svm_test1,
                "test2": li_files_svm_test2}


    #############cvm
    for (root, dirs, file) in os.walk(path_cvm):
        for dir in dirs:
            li_dir_cvm.append(dir)
            print(dir)

    for (root, dirs, file) in os.walk(path_cvm + '/' + li_dir_cvm[0]):
        for f in file:
            li_files_cvm_test1.append(f)

    for (root, dirs, file) in os.walk(path_cvm + '/' + li_dir_cvm[1]):
        for f in file:
            li_files_cvm_test2.append(f)

    dict_cvm = {"test1": li_files_cvm_test1,
            "test2": li_files_cvm_test2}



    res = {"svm" : dict_svm,
           "cvm" : dict_cvm}

    return res


@app.route('/index-results')
def res():
    li_cvm = []
    li_svm = []

    ########svm
    for (root, dirs, file) in os.walk(path_svm):
        for f in file:
            print(f)
            li_svm.append(f)


    df_text_file_svm = pd.read_csv(path_svm + '/test1/' + li_svm[1]).to_dict()

    html_link_svm = pathlib.Path('//'+path_svm + '/test1/' + li_svm[0]).as_uri()



    dict_svm = {"html File": html_link_svm,
             "text file results": df_text_file_svm}



    ########cvm
    for (root, dirs, file) in os.walk(path_cvm):
        for f in file:
            li_cvm.append(f)


    df_text_file = pd.read_csv(path_cvm + '/test1/' + li_cvm[1]).to_dict()

    html_link = pathlib.Path('//'+path_cvm + '/test1/' + li_cvm[0]).as_uri()

    dict_cvm = {"html File": html_link,
             "text file results": df_text_file}

    res = {"cvm": dict_cvm,
           "svm" : dict_svm}


    return res

app.run(host='0.0.0.0',port=5500)