from App import app

if __name__ == "__main__":
	app.run(debug=True,port=5000)

from flask import Flask, render_template
app = Flask(__name__)
