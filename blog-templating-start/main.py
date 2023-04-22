from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url = 'https://api.npoint.io/4af156202f984d3464c3')
    response.raise_for_status()
    posts = [{'id': post['id'],'title': post['title'], 'subtitle': post['subtitle'], 'body': post['body']} for post in response.json()]
    return render_template("index.html", blogs = posts)

@app.route('/detail-blog/<id>')
def detail_blog(id):
    response = requests.get(url = f'https://api.npoint.io/4af156202f984d3464c3/{id}')
    response.raise_for_status()
    data = response.json()
    print(data)
    post = Post(data['title'], data['subtitle'], data['body'])
    return render_template("post.html", blog = post)

if __name__ == "__main__":
    app.run(debug=True)
