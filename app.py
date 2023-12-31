from flask import Flask
from flask_cors import CORS
from src.services.ChromeUXReportService import *

app=Flask(__name__)
CORS(app,methods=['GET','POST'])

@app.route('/get-defaults',methods=['GET'])
def getDefaultConfigs():
    return ChromeUXReportService.getDefaultConfigs()

@app.route('/get-ux-report',methods=['POST'])
def getPageUXReport():
    return ChromeUXReportService.getPageUXReport()

app.run(host=0.0.0.0,port=10000)
