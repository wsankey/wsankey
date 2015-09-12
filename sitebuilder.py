import sys

from flask import Flask, render_template, render_template_string, Markup, redirect, url_for
from flask_flatpages import FlatPages, pygmented_markdown
from flask_frozen import Freezer

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite']

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)

def prerender_jinja(text):
    prerendered_body = render_template_string(Markup(text))
    return pygmented_markdown(prerendered_body)

app.config['FLATPAGES_HTML_RENDERER'] = prerender_jinja

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/aboutme")
def aboutme():
	return render_template('aboutme.html')

@app.route("/projects")
def projects():
	return render_template('projects.html')

@app.route("/posts/")
def blog():
	articles = (p for p in pages if "date" in p.meta)
	latest = sorted(articles, reverse=True, 
							key=lambda p: p.meta['date'])
	return render_template('blog.html', pages=latest)

@app.route('/tag/<string:tag>/')
def tag(tag):
	if tag == "FivePy":
		return redirect(url_for('fivepy'))
	else:
		tagged = [p for p in pages if tag in p.meta.get('tags', [])]
		return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/posts/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)

@app.route('/fivepy/')
def fivepy():
	posts = [p for p in pages if p.meta['tags'] == ['FivePy']]
	return render_template('fivepy.html', pages=posts)

if __name__ == "__main__":
	app.run(port=8000)
