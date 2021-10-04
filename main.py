from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	# Index page

	with open(r"/home/arghya/Github/Hack Lists/hackathonList.txt", 'r') as hl:
		data = hl.readlines()

	return render_template('index.html', contests=data)

if __name__ == '__main__':
	app.run(debug=True)