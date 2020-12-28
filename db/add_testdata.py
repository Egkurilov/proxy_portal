from sqlalchemy.orm import sessionmaker

from db import migrate
from db.migrate import ProxyList

DBSession = sessionmaker(bind=migrate.engine)
session = DBSession()


NewProject = ProxyList(id = 10,
                    project = 'Заказ дебетовой карты в мобильном приложении',
                    proxy_port_in = '30100',
                    proxy_name = 'Audit',
                    fp_name = 'CARDS_MOBILE',
                    author = 'Kurilov-EI',
                    proxy_port_out='33100',
                    stop_date = '9/16/2016 20:00',
                    start_date = '9/16/2016 21:00',
                    status = 1)


session.add(NewProject)
session.commit()
session.flush()
