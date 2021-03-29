from flask import Flask
from flask import request
import json
import os
import sys
 
import merge_info
import get_last_week

app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/bangumi')
def get_bangumi_info():
    bangumi = merge_info.merge_info()
    return bangumi

@app.route('/lastweek')
def get_last_week_info():
    last_week = get_last_week()
    return last_week


if __name__ == '__main__':
    app.run(
      #host='0.0.0.0',
      port= 80,
      debug=True
    )
##