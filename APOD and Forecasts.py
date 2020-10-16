from bs4 import BeautifulSoup as bs
import requests
import time
from flask import Flask
global qum
qum = "'"
global buttons
buttons = '<button onclick="location.href=' + qum + "/" + qum + ';">APOD and Forecast</button>' + '<button onclick="location.href=' + qum + "/apod" + qum + ';">APOD</button>' + '<button onclick="location.href=' + qum + "/forecast" + qum + ';">Forecast</button>' + '<button onclick="location.href=' + qum + "/pi" + qum + ';">Pi Version</button>'



def daily_astronomy():
    global backupImage
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    s1 = 'src="image'
    i1 = d2.split(s1,1)[1]
    s2 = '"'
    i2 = i1.split(s2,1)[0]
    if type(i2) is str:
        backupImage = i2
    else:
        i2 = backupImage

    s3 = '<center>\n<b>'
    i3 = d2.split(s3,1)[1]
    s4 = '<p> <center>'
    i4 = i3.split(s4,1)[0]

    #ob = "{"
    #stylesheet = '<style>button' + ob + 'top: 0;}</style>'
    

    forecast = '</div><div class="column right"><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"></div></div></body>'
    columns = '<head><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title>'
    write_this = (columns + '<br><img src="https://apod.nasa.gov/apod/image' + i2 +'">\n<centre>\n<b><br/>' + i4 + forecast)
    thisone = write_this
    return thisone


def pi_daily_astronomy():
    global backupImage
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    s1 = 'src="image'
    i1 = d2.split(s1,1)[1]
    s2 = '"'
    i2 = i1.split(s2,1)[0]
    if type(i2) is str:
        backupImage = i2
    else:
        i2 = backupImage

    s3 = '<center>\n<b>'
    i3 = d2.split(s3,1)[1]
    s4 = '<p> <center>'
    i4 = i3.split(s4,1)[0]

    forecast = '</div><div class="column right"><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C" width=350><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C" width=350></div></div></body>'
    columns = '<head><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><head><meta name="viewport"content="width=device-width, initial-scale=1"><style>*{box-sizing: border-box;}.column{float: left;}.left{width:640px;}.row:after{content: "";  display: table;  clear: both;}</style></head><body><div class="row"><div class="column left">'
    write_this = (columns + '<br><img src="https://apod.nasa.gov/apod/image' + i2 +'" height=300>\n<centre>\n<b><br/>' + i4 + forecast)
    thisone = write_this
    return thisone

def getApod():
    global backupImage
    global thisone
    url = 'https://apod.nasa.gov/apod/astropix.html'
    req = requests.get(url)
    soup = bs(req.content, 'html.parser')
    d2 = str(soup)
    s1 = 'src="image'
    i1 = d2.split(s1,1)[1]
    s2 = '"'
    i2 = i1.split(s2,1)[0]
    if type(i2) is str:
        backupImage = i2
    else:
        i2 = backupImage

    s3 = '<center>\n<b>'
    i3 = d2.split(s3,1)[1]
    s4 = '<p> <center>'
    i4 = i3.split(s4,1)[0]

    return '<head><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><br><img src="https://apod.nasa.gov/apod/image' + i2 + '"\n<centre>\n<b><br/>' + i4

def getForecast():
    return '<head><meta http-equiv="refresh" content="3600"><link rel="icon"href="https://apod.nasa.gov/favicon.ico">' + buttons + '</head><title>Daily Astronomy</title><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g7.ASP?LOCATIONID=59641&CO=UK&U=C"><br><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24_h_astronomy.ASP?LOCATIONID=59641&CO=UK&U=C"><img src="https://www.metcheck.com/TRIGGERS/STICKIES/g24.ASP?LOCATIONID=59641&CO=UK&U=C">'

app = Flask(__name__)

@app.route('/')
def apod_forecast():
    try:
        return daily_astronomy()
    except:
        print ('APOD FORECAST LOOP')

@app.route('/pi')
def pi_apod_forecast():
    try:
        return pi_daily_astronomy()
    except:#may be redundant
        print('PI APOD FORECAST LOOP')
        time.sleep(3600)

@app.route('/apod')
def onlyApod():
    try:
        return getApod()
    except:
        print ('GET APOD EXCEPTION')
        time.sleep(3600)

@app.route('/forecast')
def onlyForecast():
    try:
        return getForecast()
    except:
        print ('GET FORECAST EXCEPTION')
        time.sleep(3600)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port='8080')
