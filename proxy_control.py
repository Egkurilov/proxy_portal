from flask import session
from sqlalchemy.orm import sessionmaker
from db import migrate
from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def start_proxy(ids):
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': True})
    session.flush()
    session.commit()


def stop_proxy(ids):
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': False})
    session.flush()
    session.commit()
