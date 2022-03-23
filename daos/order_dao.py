from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

from daos.status_dao import StatusDAO
from db import Base


class OrderDAO(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True) 
    customer_id = Column(String)
    product_id = Column(String)
    order_date = Column(DateTime)
    delivery_date = Column(DateTime)
    # reference to status as foreign key relationship. This will be automatically assigned.
    status_id = Column(Integer, ForeignKey('status.id'))
    # https: // docs.sqlalchemy.org / en / 14 / orm / basic_relationships.html
    # https: // docs.sqlalchemy.org / en / 14 / orm / backref.html
    status = relationship(StatusDAO.__name__, backref=backref("delivery", uselist=False))

    def __init__(self, customer_id, product_id, order_date,delivery_date, status):
        self.product_id = product_id
        self.customer_id = customer_id
        self.order_date = order_date
        self.delivery_date = delivery_date
        self.status = status
