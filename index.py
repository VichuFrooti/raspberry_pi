from flask import Flask
from flask_cors import CORS, cross_origin
import RPi.GPIO as GPIO

app = Flask(__name__)
cors = CORS(app)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(40, GPIO.LOW)
GPIO.setup(38, GPIO.LOW)
GPIO.setup(36, GPIO.LOW)
GPIO.setup(32, GPIO.LOW)

@app.route('/e40')
def e40():
    GPIO.output(40, GPIO.HIGH)
@app.route('/e38')
def e40():
    GPIO.output(38, GPIO.HIGH)
@app.route('/e36')
def e40():
    GPIO.output(36, GPIO.HIGH)
@app.route('/e32')
def e40():
    GPIO.output(32, GPIO.HIGH)  

@app.route('/d40')
def d40():
    GPIO.output(40, GPIO.LOW)
@app.route('/d38')
def d40():
    GPIO.output(38, GPIO.LOW)
@app.route('/d36')
def d40():
    GPIO.output(36, GPIO.LOW)
@app.route('/d32')
def d40():
    GPIO.output(32, GPIO.LOW)

app.config['CORS_HEADERS'] = 'Content-Type'
if __name__ == '__main__':
    app.run(debug=True, port=8080, host='127.0.0.1')