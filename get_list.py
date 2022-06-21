import pathlib

from flask import Flask, jsonify, redirect, url_for
import os

app = Flask(__name__)


@app.route('/get_list', methods=['GET'])
def get_data():
    try:
        l_o_cvm_folders = []
        l_o_svm_folders = []
        l_o_cvm_files = []
        l_o_svm_files = []

        path1 = r"C:/Users/Anjana/OneDrive/Desktop/Task/cvm"
        path2 = r"C:/Users/Anjana/OneDrive/Desktop/Task/svm"

        for (root1, dirs1, file1) in os.walk(path1):
            for i in dirs1:  # Test1
                l_o_cvm_folders.append(i)
                cvm_files_contents = []
                for filename in os.listdir(path1 + "/" + i):  # path inside Test1
                    # if its a text file read data, if it html file give url of the file.
                    if filename.endswith(".txt"):
                        with open(path1 + "/" + i + "/" + filename, 'r') as txt_file:
                            data = txt_file.read()
                        dt = {filename: data}
                    elif filename.endswith(".html"):
                        link = pathlib.Path(path1 + "/" + i + "/" + filename).as_uri()
                        dt = {filename: link}
                    else:
                        return jsonify({"error": "invalid file format!!"})
                    cvm_files_contents.append(dt)  #
                    # l=[filename if filename.endswith(.txt)]
                cvm = {"cvm": cvm_files_contents}
                print(cvm)
                l_o_cvm_files.append({i: cvm})
        # print(l_o_cvm_folders)
        # print(l_o_cvm_files)

        for (root1, dirs1, file1) in os.walk(path2):
            for i in dirs1:  # Test1
                l_o_svm_folders.append(i)
                svm_files_contents = []
                for filename in os.listdir(path2 + "/" + i):  # path inside Test1
                    if filename.endswith(".txt"):
                        with open(path2 + "/" + i + "/" + filename, 'r') as txt_file:
                            data = txt_file.read()
                        dl = {filename: data}
                    elif filename.endswith(".html"):
                        link = pathlib.Path(path2 + "/" + i + "/" + filename).as_uri()
                        dl = {filename: link}
                    else:
                        return jsonify({"error": "invalid file format!!"})
                    svm_files_contents.append(dl)
                    # l=[filename if filename.endswith(.txt)]
                svm = {"svm": svm_files_contents}
                print(svm)
                l_o_svm_files.append({i: svm})

        print(l_o_cvm_files)
        print(l_o_svm_files)
        return jsonify(l_o_svm_files, l_o_cvm_files)

    except Exception as e:
        return jsonify(e)


if __name__ == '__main__':
    app.run(port=5500, debug=True)
