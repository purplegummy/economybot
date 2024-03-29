from fastapi import FastAPI, Depends, HTTPException, Response
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
      return member

  

@app.post("/addMember")
async def member(request: MemberCreate, db: Session=Depends(get_db)):
        member = Member(memberId=request.memberId, money=request.money)
        db.add(member)
        db.commit()
        db.refresh(member)
        return member

@app.post("/updateMember")
async def updateMember(request: MemberCreate, db: Session=Depends(get_db)):
        db.query(Member).filter(Member.memberId == request.memberId).update({'memberId': request.memberId, 'money': round(request.money, 2)})
        db.commit()
        db.refresh()
        
@app.get('/leaderboard')
async def leaderboard(db: Session=Depends(get_db)):
      #get the members with the 3 highest values for money  and   money
      

      print("Server -")
      
      topThree = db.query(Member).order_by(Member.money.desc()).limit(3).all()
      #get information on 3 highest values for money  and   money
      print(topThree)
      return topThree
@app.post("/buystock")
async def buyStock(request: StocksCreate, db: Session=Depends(get_db)):
      stock = Stocks(member_id=request.member_id, buyPrice=request.buyPrice, shares=request.shares, buyTime=datetime.now())
      db.add(stock)
      db.commit()
      db.refresh(stock)


    





