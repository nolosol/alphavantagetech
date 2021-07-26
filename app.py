from flask import Flask
from flask import render_template
from flask import jsonify
from flask import session
import requests

app = Flask(__name__)
app.config["SECRET_KEY"]="J7B204Ep8G9whbWpVrk7rQ"
@app.route("/home/<APIkey>")
def testingindex(APIkey):
    session["SessionId"]=APIkey
    return  render_template("datalist.html") 
@app.route("/in/<sym>")
def index(sym,methods=["POST","GET"]):
    sym_name={}
    str_url="https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+sym+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    for items in data["bestMatches"]:
        sym_name.update({items["1. symbol"]:items["2. name"]})
    print(sym)
    return jsonify(sym_name)
@app.route("/grid/<sym>")
def showgrid(sym,methods=["POST","GET"]):
    print(sym)
    sym_name={}
    str_url="https://www.alphavantage.co/query?function=SYMBOL_SEARCH&keywords="+sym+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    for items in data["bestMatches"]:
        sym_name["symbol"]=items["1. symbol"]
        sym_name["name"]=items["2. name"]
        sym_name["type"]=items["3. type"]
        sym_name["region"]=items["4. region"]
        sym_name["marketOpen"]=items["5. marketOpen"]
        sym_name["marketClose"]=items["6. marketClose"]
        sym_name["timezone"]=items["7. timezone"]
        sym_name["currency"]=items["8. currency"]
        sym_name["matchScore"]=items["9. matchScore"]
    print(sym)
    return jsonify(sym_name)
@app.route("/intraday/<cmpny>/<interval>")
def intraday(interval,cmpny,methods=["POST","GET"]):
    str_url="https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol="+cmpny+"&interval="+interval+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    data=data["Time Series ("+interval+")"]
    return jsonify(data)
@app.route("/dailyview/<cmpny>")
def  dailyview(cmpny,methods=["POST","GET"]):
    str_url="https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol="+cmpny+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    data=data["Time Series (Daily)"]
    print(str_url)
    print(data)
    return jsonify(data)
@app.route("/weeklyview/<cmpny>")
def  weeklyview(cmpny,methods=["POST","GET"]):
    str_url="https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol="+cmpny+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    data=data["Weekly Time Series"]
    return jsonify(data)
@app.route("/monthlyview/<cmpny>")
def  monthlyview(cmpny,methods=["POST","GET"]):
    str_url="https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol="+cmpny+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    data=data["Monthly Time Series"]
    return jsonify(data)
@app.route("/GlobalQuoteView/<cmpny>")
def  GlobalQuoteView(cmpny,methods=["POST","GET"]):
    sym_name={}
    str_url="https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+cmpny+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    print(data["Global Quote"])
    sym_name["symbol"]=data["Global Quote"]["01. symbol"]
    sym_name["open"]=data["Global Quote"]["02. open"]
    sym_name["high"]=data["Global Quote"]["03. high"]
    sym_name["low"]=data["Global Quote"]["04. low"]
    sym_name["price"]=data["Global Quote"]["05. price"]
    sym_name["volume"]=data["Global Quote"]["06. volume"]
    sym_name["latest_trading_day"]=data["Global Quote"]["07. latest trading day"] 
    sym_name["previous_close"]=data["Global Quote"]["08. previous close"]
    sym_name["change"]=data["Global Quote"]["09. change"]
    sym_name["change_percent"]=data["Global Quote"]["10. change percent"]
    return jsonify(sym_name)
@app.route("/indicatorView/<cmpny>/<time_period>/<interval>/<series_type>")
def  indicatorView(cmpny,time_period,interval,series_type,methods=["POST","GET"]):
    str_url="https://www.alphavantage.co/query?function=SMA&symbol="+cmpny+"&interval="+interval+"&time_period="+time_period+"&series_type="+series_type+"&apikey="+session["SessionId"]
    data= requests.get(str_url).json()
    data=data["Technical Analysis: SMA"]
    return jsonify(data)
