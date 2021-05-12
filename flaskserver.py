"""
This server consists of various app routes defined to perform specific tasks.
When the function is triggered with parameters from the API POST request, powershell script for
the corresponding function is innoked in the subprocess to perform the task and returns the result to the API.
This script can be used for bulk user creation at a very faster pace.
It is observed that 1000 users can be created within a minute.

"""
from flask import Flask,request
import requests
import sys
from flask import jsonify
import subprocess
from subprocess import Popen, PIPE
import json
import re
import os

app = Flask(__name__)

@app.route('/create',methods=['POST'])
def createuser():
        d=request.get_json()
        arr=""
        final =[]
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        scriptPath = os.path.join(fileDir, 'scripts\createUser.ps1')
        for x in d['users']:
                username=x['employeeUsername']
                password=x['employeePassword']
                upn=x['domainName']
                arr=arr+username+","+password+","+upn+"-"
        process = subprocess.Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', scriptPath, arr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        x = out.decode()
        print(x)
        y = x.splitlines()
        for result in y:
            if result.endswith('created successfully'):
                value = 'true'
            else:
                value = 'false'
                break
        if value == 'true':
            return jsonify(success="true",message=y),200
        else:
            return jsonify(success="false",message=y),500

@app.route('/resetPassword',methods=['POST'])
def resetpassword():
        d=request.get_json()
        arr=""
        decoded = d
        final =[]
        arr=d['username']+","+d['password']+"-"
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        scriptPath = os.path.join(fileDir, 'scripts\\resetPassword.ps1')
        process = Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', scriptPath, arr], stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        x = out.decode()
        print(x)
        if x.startswith("Password changed successfully"):
            return jsonify(success="true",message=x),200
        else:
            return jsonify(success="false",message=x),500

@app.route('/delete',methods=['POST'])
def deleteuser():
        d=request.get_json()
        arr=""
        decoded = d
        final =[]
        print(decoded)        
        arr=d['username']+"-"
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        scriptPath = os.path.join(fileDir, 'scripts\deleteuser.ps1')
        process = Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', scriptPath, arr], stdout=PIPE, stderr=PIPE)
        out, err = process.communicate()
        x = out.decode()
        print(x)
        if x.endswith('successfully\n'):
            return jsonify(success="true",message=x),200
        else:
            return jsonify(success="false",message=x),500

@app.route('/api/user/book',methods=['POST'])
def bookslot():
        d=request.get_json()
        arr=""
        final =[]
        
        arr=d['username']+","+d['bookingday']+","+d['bookingtime']+"*"
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        scriptPath = os.path.join(fileDir, 'scripts\bookslot.ps1')
        process = subprocess.Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', scriptPath, arr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        x = out.decode()
        print(x)
        if x.endswith('completed successfully. \n'):
            return jsonify(success="true",message=x),200
        else:
            return jsonify(success="false",message=x),500

@app.route('/api/user/cancel',methods=['POST'])
def cancelslot():
        d=request.get_json()
        arr=""
        decoded = d
        final =[]
        fileDir = os.path.dirname(os.path.realpath('__file__'))
        scriptPath = os.path.join(fileDir, 'scripts\cancelslot.ps1')
        arr=d['username']+"*"
        process = subprocess.Popen(['C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe', scriptPath, arr], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        x = out.decode()
        print(x)
        if x.startswith('slots removed'):
            return jsonify(success="true",message=x),200
        else:
            return jsonify(success="false",message=x),500

@app.route('/',methods=['GET'])
def temp():
        return "Server Running on port 8006 :)"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8006)
        app.run(threaded=true)
