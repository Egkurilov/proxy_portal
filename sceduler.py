import datetime

from sqlalchemy.orm import sessionmaker

from db import migrate
from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


def view_db():
    #datetimenow = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    test_data = "28.12.2020 13:10"
    record_to_kill = session.query(ProxyList.id, ProxyList.proxy_pid, ProxyList.start_date, ProxyList.stop_date) \
        .filter(ProxyList.stop_date == test_data)

    for record_to_kills in record_to_kill:
        if record_to_kills is None:

            print(record_to_kills + " is Null")
        else:
            print(record_to_kills)


view_db()

