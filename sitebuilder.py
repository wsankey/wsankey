import sys

from flask import Flask, render_template, render_template_string, Markup
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
	ordered = [p for p in sorted(pages)]
	return render_template('blog.html', pages=ordered)

@app.route('/tag/<string:tag>/')
def tag(tag):
	tagged = [p for p in pages if tag in p.meta.get('tags', [])]
	return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/posts/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	return render_template('page.html', page=page)
	
if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(port=8000)
