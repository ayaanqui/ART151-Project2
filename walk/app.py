import re
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    page = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    data = BeautifulSoup(page.content, 'html.parser')
    title = data.find('h1', {"id": "firstHeading"}).text
    content = data.find('p').text

    return render_template('index.html', context={"content":  content, "title": title})
