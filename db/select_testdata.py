from sqlalchemy.orm import sessionmaker

from db import migrate
from db.migrate import ProxyList as pl

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()

def get_query():
    query_result = session.query(pl).all()
    print(query_result)
    return query_result

get_query()