from flask import Flask,render_template
app = Flask(__name__)
@app.route('/') # current directory path
def home():
	return render_template('/home.html',title="HospitalZone")
@app.route('/appointment')
def appointment():
	return render_template('/appointment.html',title="New Patient")
@app.route('/contactus')
def contactus():
	return render_template('/contactus.html',title='Reach-us')