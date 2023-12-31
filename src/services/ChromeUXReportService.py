from flask import jsonify,request
from src.utils.APIConstants import *
from src.utils.AppConstants import *
import requests

class ChromeUXReportService:
    def getDefaultConfigs():
        return jsonify(labels)
    
    def getPageUXReport():
        """
        Fetch ux date for the provided urls
        """
        try:
            response=[]
            urls=request.get_json()
            if len(urls)>0:
                for url in urls:
                    obj = {
                        "origin": url,
                        "formFactor": FROM_FACTOR,
                        "metrics":METRIX
                    }
                    api_data=requests.post(API_URL,obj)
                    response.append(api_data.json()['record'])
            return response
        except Exception:
            raise Exception