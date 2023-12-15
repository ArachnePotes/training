'''
Question 25
Level 1

Question:
    Define a class, which have a class parameter and have a same instance parameter.

Hints:
    Define a instance parameter, need add it in __init__ method
    You can init a object with construct parameter or set the value later
'''

class wallet():
    balance = 0
    def __init__(self,_id,balance = None):
        self._id  = _id
        self.balance = balance
    def putMoney(self,amount):
        self.balance += amount
    def getbalance(self):
        return self.balance
        
w = wallet(1,balance=500)        
w2 =  wallet(2)

print(f'w:{w.getbalance()}\nw2:{w2.getbalance()}')
