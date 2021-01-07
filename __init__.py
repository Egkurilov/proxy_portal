from flask import Flask
from sqlalchemy import create_engine


engine = create_engine('sqlite:///proxy_list.db?check_same_thread=False')

app = Flask(__name__)


def create_app():
    app = Flask(__name__)

    app.config['host'] = '0.0.0.0'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///proxy_list.db?check_same_thread=False'

