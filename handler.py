from sqlalchemy.orm import sessionmaker

from db import migrate
from db.migrate import ProxyList
from proxy_control import start_proxy, stop_proxy

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def handler_command(command, id):
    if command == 'start':
        start_proxy(id)
    elif command == 'stop':
        stop_proxy(id)
    elif command == 'edit':
        print(command)


def get_params(request):
    proxy_port_in = request['proxy_port_in']
    proxy_name = request['proxy_name']
    fp_name = request['fp_name']
    project = request['project']
    author = request['author']
    proxy_port_out = request['proxy_port_out']
    stop_date = request['stop_date']
    start_date = request['start_date']
    status = request['status']
    into_db(proxy_port_in, fp_name, author, stop_date, start_date, proxy_port_out, project, proxy_name)


def into_db(proxy_port_in, fp_name, author, stop_date, \
            start_date, proxy_port_out, project, proxy_name):
    insert_new_proxy = ProxyList(
        project=project,
        proxy_port_in=proxy_port_in,
        proxy_name=proxy_name,
        fp_name=fp_name,
        author=author,
        proxy_port_out=proxy_port_out,
        stop_date=stop_date,
        start_date=start_date,
        status=1)
    session.add(insert_new_proxy)
    session.flush()
    session.commit()
