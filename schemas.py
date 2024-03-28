from pydantic import BaseModel
from models import Member, Stocks
from datetime import datetime
from typing import List

class StocksBase(BaseModel):
    member_id:int
    buyPrice: float
    shares: int
    stockName: str
 

class StocksCreate(StocksBase):
    pass
class StocksSchema(StocksBase):
    id: int
    buyTime: datetime
    
  

class MemberBase(BaseModel):
    memberId: int
    money: float
    stocks: List[StocksSchema] = []
    class Config:
        orm_mode = True

class MemberCreate(MemberBase):
    pass

class MemberSchema(MemberBase):
    id: int
  
