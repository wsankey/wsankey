from flask import Flask, render_template
from flask_flatpages import FlatPages

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

@app.route("/")
def index():
	return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
    return pages.get_or_404(path).html

if __name__ == "__main__":
    app.run(port=8000)