import requests
import json
import calendar

url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

querystring = {"q":"Karachi"}

headers = {
	"X-RapidAPI-Key": "fb2198e511msh6763854ca1dd8bcp1306cajsn7c56156d7038",
	"X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
}

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

querystring = {"q":"Karachi","days":"3"}
response = requests.request("GET", url, headers=headers, params=querystring)
json_data = json.loads(response.text)

TomHi=json_data['forecast']['forecastday'][0]['day']
TomLo=json_data['forecast']['forecastday'][0]['day']['mintemp_c']
TomCon=json_data['forecast']['forecastday'][0]['day']['condition']['icon']

DAHi=json_data['forecast']['forecastday'][1]['day']['maxtemp_c']
DALo=json_data['forecast']['forecastday'][1]['day']['mintemp_c']
DACon=json_data['forecast']['forecastday'][1]['day']['condition']['icon']

N2N=json_data['forecast']['forecastday'][2]['date']
N2NHi=json_data['forecast']['forecastday'][2]['day']['maxtemp_c']
N2NLo=json_data['forecast']['forecastday'][2]['day']['mintemp_c']
N2NCon=json_data['forecast']['forecastday'][2]['day']['condition']['icon']
print(N2N)
