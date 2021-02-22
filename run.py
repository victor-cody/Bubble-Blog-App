from flaskblog import app

if __name__ == "__main__":
	app.run(debug=True, host='0.0.0.0', port=8000)

from flask import Flask, render_template
app = Flask(__name__)
