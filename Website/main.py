from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	# Index page

	with open(r"C:\Users\argsa\OneDrive\Documents\GitHub\academia\Python\Python Projects\Hackathon Lists\hackathonList.txt", 'r') as hl:
		data = hl.readlines()

	return render_template('index.html', contests=data)

if __name__ == '__main__':
	app.run(debug=True)