from flask import Flask
from app import app
import config as config

if __name__=='__main__':
	app.run(host='0.0.0.0',debug=config.DEBUG)