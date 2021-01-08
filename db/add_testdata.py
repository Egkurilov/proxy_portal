from sqlalchemy.orm import sessionmaker

from db import migrate
from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


x = session.query(ProxyList.proxy_pid).filter(ProxyList.id == "3")

for XX in x:
    print(XX[0])