from flask import Flask, render_template
import requests
import re

app = Flask(__name__)

@app.route('/')
def image_viewer():
    source = "https://www.bing.com/images/search?q=gojo&form=HDRSC3&pc=EMMX01&first=1"
    data = str(requests.get(source).content)
    pattern = r'https:\/\/[^\s"&]+\.jpg'
    matches = re.findall(pattern, data)
    
    return render_template('index.html', image_urls=matches)

if __name__ == '__main__':
    app.run()
