import os

from flask import session
from sqlalchemy.orm import sessionmaker
from db import migrate
from db.migrate import ProxyList
import subprocess
from threading import Thread

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def execute_shell_script(ids):
    result_sh = subprocess.Popen(['/home/shaneque/work/proxy_portal/static/proxy_files/proxy.sh', "abc"], \
                                 stdout=subprocess.PIPE, shell=True)
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'proxy_pid': result_sh.pid})
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': True})
    session.flush()
    session.commit()


def start_proxy(ids):
    th = Thread(target=execute_shell_script, args=(ids,))
    th.start()


def stop_proxy(ids):

    kill_pid = session.query(ProxyList.id, ProxyList.proxy_pid).filter(ProxyList.id == ids)
    print("ID in base: "+ ids)
    for pid in kill_pid:
        print("PID " + pid[0])
        subprocess.Popen(['kill -9 ' + pid[0]], shell=True)
    session.query(ProxyList.id).filter(ProxyList.id == ids).update({'status': False})
    session.flush()
    session.commit()


def delete_proxy(ids):
    session.query(ProxyList.id).filter(ProxyList.id == ids).delete()
    session.flush()
    session.commit()
