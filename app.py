import requests as requests
from flask import Flask,render_template
from bs4 import BeautifulSoup

app = Flask(__name__)
@app.route('/', methods=['GET','POST'])
def index():
    url = "https://www.businesstoday.in/technology"
    req = requests.get(url)
    soup = BeautifulSoup(req.content,"html.parser")
    outer_data = soup.find_all('div',class_='widget-listing',limit=5)
    finalnews = ""
    for data in outer_data:
        news = data.div.div.a["title"]
        finalnews += " \u2022 " +news +"\n"
    # print(finalnews)
    return render_template('index.html',NewsUpdate=finalnews)


if __name__ == "__main__":
    app.run(debug=True)

