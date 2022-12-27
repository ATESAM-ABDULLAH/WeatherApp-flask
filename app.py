import json
import requests
import calendar
from fpdf import FPDF
from flask import Flask,request,render_template

API_KEY = "fb2198e511msh6763854ca1dd8bcp1306cajsn7c56156d7038"
API_HOST = "weatherapi-com.p.rapidapi.com"
API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_weather',methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        q = request.form['location']
        url = API_URL
        querystring = {"q":q}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        try:
            response = requests.request("GET", url, headers=headers, params=querystring)
            json_data = json.loads(response.text)
            
            name = json_data['location']['name']
            region = json_data['location']['region']
            country = json_data['location']['country']
            tz_id = json_data['location']['tz_id']
            localtime = json_data['location']['localtime']
            last_updated = json_data['current']['last_updated']
            temp_c = json_data['current']['temp_c']
            is_day = json_data['current']['is_day']
            condition_text = json_data['current']['condition']['text']
            condition_icon = json_data['current']['condition']['icon']
            precip_mm = json_data['current']['precip_mm']
            humidity = json_data['current']['humidity']
            feelslike_c = json_data['current']['feelslike_c']
            
            querystring = {"q":q,"days":"3"}
            url="https://weatherapi-com.p.rapidapi.com/forecast.json"
            response = requests.request("GET", url, headers=headers, params=querystring)
            json_data = json.loads(response.text)
            
            TomHi=json_data['forecast']['forecastday'][0]['day']['maxtemp_c']
            TomLo=json_data['forecast']['forecastday'][0]['day']['mintemp_c']
            TomCon=json_data['forecast']['forecastday'][0]['day']['condition']['icon']
            
            DAHi=json_data['forecast']['forecastday'][1]['day']['maxtemp_c']
            DALo=json_data['forecast']['forecastday'][1]['day']['mintemp_c']
            DACon=json_data['forecast']['forecastday'][1]['day']['condition']['icon']
            
            N2N=json_data['forecast']['forecastday'][2]['date']
            N2NHi=json_data['forecast']['forecastday'][2]['day']['maxtemp_c']
            N2NLo=json_data['forecast']['forecastday'][2]['day']['mintemp_c']
            N2NCon=json_data['forecast']['forecastday'][2]['day']['condition']['icon']
            
            x=N2N.split('-')
            N2N=str(int(x[2]+1))+" "+calendar.month_abbr[int(x[1])]

            return render_template('home.html',name=name,region=region,country=country,tz_id=tz_id,
            localtime=localtime,last_updated=last_updated,
            temp_c=temp_c,is_day=is_day,condition_text=condition_text,condition_icon=condition_icon,precip_mm=precip_mm,
            humidity=humidity,feelslike_c=feelslike_c,TomHi=TomHi,TomLo=TomLo,TomCon=TomCon,
            DAHi=DAHi,DALo=DALo,DACon=DACon,N2N=N2N,N2NHi=N2NHi,N2NLo=N2NLo,N2NCon=N2NCon)

        except:
            return render_template('home.html',error='Place Does Not Exist!')


if __name__ == '__main__':
    app.run(debug=True)
