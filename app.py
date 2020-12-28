from flask import Flask, render_template, redirect, request
from sqlalchemy.orm import sessionmaker

from db import migrate
from handler import handler_command, det_params

app = Flask(__name__)

from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


@app.route('/')
def main():
    query_result = session.query(ProxyList).all()
    return render_template('index.html', query_result=query_result)


@app.route('/comand/<comand>')
def comand(comand):
    handler_command(comand)
    return redirect('/', code=302)


@app.route('/add')
def add():
    return render_template('add.html')


@app.route('/input')
def input():
    det_params(request.args)
    return redirect('/', code=302)


if __name__ == "__main__":
    app.run(threaded=True, processes=3, port=5000)
