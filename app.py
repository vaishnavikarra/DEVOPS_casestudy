from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace with your own API key from https://newsapi.org
API_KEY = "27c9f4e4e3ee435a835acaaa7a56db08"

@app.route('/', methods=['GET', 'POST'])
def home():
    articles = []
    keyword = ""
    message = ""
    if request.method == 'POST':
        keyword = request.form.get('keyword')
        if keyword:
            url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}&language=en&pageSize=10'
            response = requests.get(url)
            data = response.json()

            if data.get("status") == "ok":
                articles = data.get("articles", [])
                if not articles:
                    message = "No articles found. Try a different keyword!"
            else:
                message = "Error fetching news. Please check your API key or connection."
        else:
            message = "Please enter a keyword to search."

    return render_template('index.html', articles=articles, keyword=keyword, message=message)


if __name__ == '__main__':
 

    app.run(host='0.0.0.0',port="5001",debug=True)
