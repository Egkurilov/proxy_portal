from flask import session
from sqlalchemy.orm import sessionmaker
from db import migrate
from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def start_proxy(ids):
    value = session.query(ProxyList.id).filter(id == 0)
    print(value)
    value.status = True
    session.commit()
    session.flush()


def stop_proxy(ids):
    value = session.query(ProxyList.id, ProxyList.status).filter(id == 0)
    print(value)
    value.status = False
    session.commit()
    session.flush()
