from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	# Index page
	with open("./tmp/hackathonListAll.txt", 'r') as hl:
		data = hl.readlines()
	return render_template('index.html', contests=data, sts="All")

@app.route('/ongoing')
def filter_ongoing():
	with open("./tmp/hackathonList.txt", 'r') as hl:
		data = hl.readlines()

	return render_template('index.html', contests=data, sts="Ongoing")


@app.route('/upcoming')
def filter_upcoming():
	with open("./tmp/hackathonListUpcoming.txt", 'r') as hl:
		data = hl.readlines()

	return render_template('index.html', contests=data, sts="Upcoming")

if __name__ == '__main__':
	app.run(debug=True)