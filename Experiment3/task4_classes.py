class Launch:#订餐管理
    def __init__(self):
        self.cust=Customer()
        self.empl=Employee()
    def order(self,foodname):
        self.cust.placeOrder(foodname,self.empl)
    def result(self,txt):
        self.cust.printfood(txt)

class Customer:#顾客类
    def __init__(self):
        self.food=[]
        self.name=None
    def placeOrder(self,foodname,employee):
        self.food.append(employee.takeOrder(foodname))
    def printfood(self,txt):
        for i in self.food:
            item='\n'+i.name
            txt.insert('end',item)
    def printcustomer(self):
        print(self.name)

class Employee:#商户类
    def __init__(self):
        self.name=None
    def takeOrder(self,foodname):
        return Food(foodname)
    def printemployee(self):
        print(self.name)

class Food:#食物类
    def __init__(self,FoodName):
        self.name=FoodName


