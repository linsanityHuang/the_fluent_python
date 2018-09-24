from flask import Flask
import time

app = Flask(__name__)


@app.route('/')
def index():
	time.sleep(3)
	return 'Hello!'


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000, debug=True)
