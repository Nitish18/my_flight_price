from flask import Flask
from app import app
import config as config

if __name__=='__main__':
	app.run(debug=config.DEBUG)