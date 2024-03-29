from dotenv import load_dotenv
import os
import requests
import json
class Player:
     def __init__(self):
        
          load_dotenv()
          self.BASE_URL = os.getenv('BASE_URL')
           
         
     async def MONEY(self, memberId: int):
        if not await self.exists(memberId):
            return None
        member = await self.getUser(memberId)
   
        return float(json.loads(member.content)["money"])
     
     async def createPlayer(self, memberId: int):
        if await self.exists(memberId):
            print("User Already Exists!")
            return
        
        user = requests.post(self.BASE_URL + "/addMember/",data=json.dumps({"memberId": memberId, "money": 2000}) )


     
     async def exists(self, memberId: int) -> bool:
         
       
         member = await self.getUser(memberId)
         if json.loads(member.content) == None:
             return False
         return True
     
     async def sendMoney(self, senderId: int, recipientId:int, money: float):
          sender = await self.getUser(senderId)
          recipient = await self.getUser(recipientId)
          sender = json.loads(sender.content)
          recipient = json.loads(recipient.content)

          if sender["money"] - money < 0:
              return False
          
          requests.post(self.BASE_URL+"/updateMember", data=json.dumps({"memberId": senderId, "money": sender["money"]-money }))
          requests.post(self.BASE_URL+"/updateMember", data=json.dumps({"memberId": recipientId, "money": recipient["money"]+money }))

          return True
     
     
     async def getUser(self, memberId: int):
          user = requests.get(self.BASE_URL+"/getMember/"+ str(memberId))
          return user
         
         