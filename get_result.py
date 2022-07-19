import pathlib
from os.path import abspath

from flask import Flask, jsonify, redirect, url_for
import os
import os.path, time

app = Flask(__name__)


@app.route('/get_result', methods=['GET'])
def get_data():
    try:
        path1 = r"demo\svm"
        path2 = r"demo\cvm"
        final = []
        for (root1, dirs1, file1) in os.walk(path1):
            for (root, dirs, file) in os.walk(path2):
                for i in dirs1:
                    for ii in dirs:
                        if i == ii:
                            files = {"testname": i, "date": time.ctime(os.path.getmtime(path1 + "/" + i))}
                            for filename in os.listdir(path1 + "/" + i):
                                if filename.endswith(".txt"):
                                    with open(path1 + "/" + i + "/" + filename, 'r') as txt_file:
                                        data = txt_file.read()
                                        files.update({"result_svm": data})
                                elif filename.endswith(".html"):
                                    pathth = abspath(path1 + "/" + i + "/" + filename)
                                    link = pathlib.Path(pathth).as_uri()
                                    files.update({"index_svm": link})
                                else:
                                    print({"error": "invalid file format!!"})
                            for filename in os.listdir(path2 + "/" + i):
                                if filename.endswith(".txt"):
                                    with open(path2 + "/" + i + "/" + filename, 'r') as txt_file:
                                        data = txt_file.read()
                                        files.update({"result_cvm": data})
                                elif filename.endswith(".html"):
                                    pathth = abspath(path2 + "/" + i + "/" + filename)
                                    link = pathlib.Path(pathth).as_uri()
                                    files.update({"index_cvm": link})
                                else:
                                    print({"error": "invalid file format!!"})
                            final.append(files)
        return jsonify({"data": final})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(port=5500, debug=True)
