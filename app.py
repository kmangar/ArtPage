from random import random, randint

from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    urls = ["https://www.gstatic.com/culturalinstitute/tabext/imax_2_1.json", "https://www.gstatic.com/culturalinstitute/tabext/imax.json"]
    
    response = requests.get(urls[randint(0, 1)])
    art_list = response.json()
    random_index = randint(0, len(art_list)-1)
    current = art_list[random_index]
    print(response.url)
    return render_template("home.html",
                           art_piece=current["title"],
                           creator=current["creator"],
                           attribution=current["attribution"],
                           art=current["image"])


if __name__ == '__main__':
    app.run(debug=True)
