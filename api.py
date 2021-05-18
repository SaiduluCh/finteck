import os
from flask import Flask, render_template, request,jsonify
from cheque_number import cheque_micr_data
from cheque_number import american_cheque_micr_data
from cheque_number import bank_of_america_cheque
import numpy as np
import base64
import cv2

app = Flask(__name__)

# @app .route('/')
# def hello():
#     return render_template('index.html')


@app.route('/', methods = ['GET', 'POST'])
def extract():
    if request.method == 'POST':
        if request.files.get("file"):
            file = request.files["file"].read()
            decoded_data = base64.b64decode(file)
            image_result = open('deer_decode.jpg', 'wb')  # cr
            image_result.write(file)
            file_path = 'deer_decode.jpg'
            data = cheque_micr_data(file_path)
            return jsonify(data)
    return render_template('index.html')


@app.route('/american_micr', methods = ['GET', 'POST'])
def american_micr():
    if request.method == 'POST':
        if request.files.get("file"):
            file = request.files["file"].read()
            decoded_data = base64.b64decode(file)
            image_result = open('decode.jpg', 'wb')  # cr
            image_result.write(file)
            file_path = 'decode.jpg'
            data = american_cheque_micr_data(file_path)
            return jsonify(data)
    return render_template('index.html')



@app.route('/bank_of_america', methods = ['GET', 'POST'])
def bank_of_america():
    if request.method == 'POST':
        if request.files.get("file"):
            file = request.files["file"].read()
            decoded_data = base64.b64decode(file)
            image_result = open('decode.jpg', 'wb')  # cr
            image_result.write(file)
            file_path = 'decode.jpg'
            data = bank_of_america_cheque(file_path)
            return jsonify(data)
    return render_template('index.html')



if __name__ == '__main__':
    app.run()
