from flask import session
from sqlalchemy.orm import sessionmaker
from db import migrate
from db.migrate import ProxyList
import subprocess
from threading import Thread

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def execute_shell_script(arg):
    argg = "--Audit"
    subprocess.call("./static/proxy_files/proxy.sh" + " " +arg + argg , shell=True)


def start_proxy(ids):
    th = Thread(target=execute_shell_script, args=(ids,))
    th.start()
    print("i'm starting", ids)

    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': True})
    session.flush()
    session.commit()


def stop_proxy(ids):
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': False})
    session.flush()
    session.commit()


def delete_proxy(ids):
    session.query(ProxyList.id).filter(ProxyList.id == ids).delete()
    session.flush()
    session.commit()
