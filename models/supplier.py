from sqlalchemy import Column,Integer,String

from config.database import Base


from sqlalchemy import Column, Integer, String

from config.database import Base


class Supplier(Base):
    
    _tablename_= "supplier"
    
    id = Column(Integer, primary_key=True)
    Name = Column(String)
    Address = Column(String)
    Phone= Column(Integer)
    Email = Column(String)
    