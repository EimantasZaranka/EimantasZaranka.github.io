import sys, os
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

app.config['FREEZER_DESTINATION'] = "docs"

freezer = Freezer(app)

@app.route('/')
def index():
	return "<h1>Comming Soon!</h1>"

if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(debug=True)