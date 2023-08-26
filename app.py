from flask import Flask, render_template, request
import requests
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def image_viewer():
    if request.method == 'POST':
        name = request.form.get('search_query')
        if not name:
            return render_template('index.html', message="Please enter a search query.")
    else:
        name = "gojo"

    source = f"https://www.bing.com/images/search?q={name}&form=HDRSC3&pc=EMMX01&first=1"
    data = str(requests.get(source).content)
    pattern = r'https:\/\/[^\s"&]+\.jpg'
    matches = re.findall(pattern, data)
    
    return render_template('index.html', image_urls=matches)

if __name__ == '__main__':
    app.run()
