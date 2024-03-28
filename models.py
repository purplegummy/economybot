from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from database import Base
from sqlalchemy.orm import relationship
class Member(Base):
    __tablename__ = "members"
    id = Column(Integer, primary_key=True, index=True)
    memberId = Column(Integer)
    money = Column(Float)
    stocks = relationship("Stocks", back_populates="member")
    
class Stocks(Base):
       __tablename__ = "stocks"
       id = Column(Integer, primary_key=True, index=True)
       member_id = Column(Integer, ForeignKey('members.id'))
       stockName = Column(String)
       member = relationship("Member",back_populates="stocks" )
       shares = Column(Integer)
       buyPrice = Column(Float)
       buyTime = Column(DateTime)