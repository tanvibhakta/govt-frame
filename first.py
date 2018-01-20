#!/usr/bin/python3
from flask import Flask
from flask import *
from frames.department import Department

app = Flask(__name__)
app._static_folder = "/static"

# , methods=['GET', 'POST']
@app.route('/')
def index():
	forest_dept = {
		'name': "Forst Dept",
		'id': '12',
		'link_from': '',
		'link_to': ''
	}
	# processes = Department(forest_dept)
	# processes.updateDatato(88888)
	# return some.getData("1234") + str(some.getDataFrom())
	return render_template('index.html')

@app.route('/list_request')
def list_request():
    return render_template('list_requests.html')


if __name__ == '__main__':
    app.run(debug=True)




# on start, spawn dashboard.
