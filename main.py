from flask import Flask,url_for,render_template,request
from bs4 import BeautifulSoup
import requests
# import pyautogui
# import time
# import instabot

app = Flask(__name__)
@app.route('/',methods=["GET"])
def index():
    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    
    finalNews=""
    for data in soup.find_all("div",class_="widget-listing",limit=6):
        news=data.div.div.a["title"]
        finalNews += '\u2022 '+news+'\n'
    #print(finalNews)

    url1 = "https://www.aajtak.in/science"
    req1 = requests.get(url1)
    soup1 = BeautifulSoup(req1.content, 'html.parser')
    
    finalNews1=""
    for data in soup1.find_all("div",class_="widget-listing",limit=6):
        news1=data.div.div.a["title"]
        finalNews1 += '\u2022 '+news1+'\n'

    # return render_template("index.html",News=finalNews)
    return render_template("index.html",News=finalNews,News1=finalNews1)


# screen size=Size(width=1920, height=1080)||| (960,1005) to go dwnbtn
    # time.sleep(5)
    # print(pyautogui.leftClick(960,1005,1))

