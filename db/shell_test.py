import subprocess

from threading import Thread


def execute_shell_script(ids):
    result = subprocess.Popen(['/home/shaneque/work/static/proxy_files/proxy.sh', ids], stdout=subprocess.PIPE, shell=True)
    print(result.pid)


def start_proxy(ids):
    th = Thread(target=execute_shell_script, args=(str(ids),))
    th.start()

start_proxy(10)