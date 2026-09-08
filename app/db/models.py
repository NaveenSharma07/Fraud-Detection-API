from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column,String,Integer,Numeric

class Base(DeclarativeBase):
    pass

class TransactionDB(Base):

    __tablename__="transactions"

    id = Column(String,primary_key=True)

    amount = Column(Numeric)

    country = Column(String)

    device = Column(String)

    score = Column(Integer)

    risk = Column(String)