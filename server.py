from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from models import Member, Stocks, Base
from schemas import MemberSchema, StocksSchema, MemberCreate, StocksCreate
from database import engine, SessionLocal
from sqlalchemy.orm import Session
from datetime import datetime
Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
        try:
            db = SessionLocal()
            yield db
        finally:
            db.close()

@app.get("/getMember/{memberId}")
async def get_member(memberId, db: Session= Depends(get_db)):
      member = db.query(Member).filter(Member.memberId == memberId).first()
      if member != None:
        return member
    

@app.post("/addMember")
async def member(request: MemberCreate, db: Session=Depends(get_db)):
        member = Member(memberId=request.memberId, money=request.money)
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

@app.post("/buystock")
async def buyStock(request: StocksCreate, db: Session=Depends(get_db)):
      stock = Stocks(member_id=request.member_id, buyPrice=request.buyPrice, shares=request.shares, buyTime=datetime.now())
      db.add(stock)
      db.commit()
      db.refresh(stock)
      return stock

    





