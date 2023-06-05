from sqlalchemy import Column, ForeignKey, Integer
from config.database import Base 


class Supplies(Base):
    __tablename__ = "supplies"

    id=Column(Integer,primary_key=True)
    supplier_id = Column(Integer,ForeignKey("supplier.id"))
    product_id = Column(Integer,ForeignKey("product.id"))
    purchase_price = Column (Integer)