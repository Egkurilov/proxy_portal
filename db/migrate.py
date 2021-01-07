# -*- coding: utf-8 -*-
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class ProxyList(Base):

    __tablename__ = 'proxy_list'

    id = Column(Integer, primary_key=True)
    proxy_pid = Column(String(2500))
    project = Column(String(2500), nullable=False, default="Имя проекта.")
    proxy_port_in = Column(Integer, nullable=False, default="32000")
    proxy_name = Column(String(2500), nullable=False)
    fp_name = Column(String(2500), nullable=False)
    author = Column(String(2500), nullable=False)
    proxy_port_out = Column(Integer, nullable=False, default="34000")
    stop_date = Column(String(2500), nullable=False)
    start_date = Column(String(2500), nullable=False)
    proxy_pid = Column(String(2500))
    status =  Column(Boolean, unique=False, default=False)


engine = create_engine('sqlite:///proxy_list.db?check_same_thread=False')

Base.metadata.create_all(engine)