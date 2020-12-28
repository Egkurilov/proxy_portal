from flask import request

from proxy_control import start_proxy, stop_proxy


def handler_command(command):
    if command == 'start':
        start_proxy()
        print(command)
    elif command == 'stop':
        print(command)
        stop_proxy()
    elif command == 'edit':
        print(command)


def det_params(request):
    proxy_port_in = request['proxy_port_in']
    fp_name = request['fp_name']
    project = request['project']
    author = request['author']
    proxy_port_out = request['proxy_port_out']
    stop_date = request['stop_date']
    start_date = request['start_date']
    status = request['status']
