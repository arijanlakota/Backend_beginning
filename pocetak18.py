from math import pi,sqrt
from datetime import datetime,date
#python object-oriented
#1
# class Circle():
#     def __init__(self,radius) -> None:
#         self.radius = radius
#     def Area(self):
#         print(self.radius**2 * pi )
#     def perimeter(self):
#         print(self.radius*2*pi)
# p1 = Circle(10)
# p1.Area()
# p1.perimeter()
#2
# class Person():
#     def __init__(self,name,country,birthDate) -> None:
#         self.name = name
#         self.country = country
#         self.birthDate = birthDate
#     def Age(self):
#         a = (datetime.now().year - datetime.fromisoformat(self.birthDate).year)
#         print(a)
#         if date.today() < datetime.date(date.today().year, datetime.fromisoformat(self.birthDate).month,datetime.fromisoformat(self.birthDate).day):
#             print(a - 1)
# p1 = Person("Arijan","Srbija",'2005-07-14')
# p1.Age()
#3
# class Calculator():
#     def __init__(self,input1,input2) -> None:
#         self.input1 = input1
#         self.input2 = input2
#     def Add(self):
#         return self.input1 + self.input2
#     def Sub(self):
#         return self.input1 - self.input2
#     def Div(self):
#         return self.input1 / self.input2
#     def Mul(self):
#         return self.input1 * self.input2
# p1 = Calculator(5,3)
# print(p1.Mul())
#4
# class Shape():
#     def __init__(self,kindShape,length) -> None:
#         self.kindShape = kindShape
#         self.length = length
#     def Area(self):
#         if self.kindShape == 'circle':
#             return self.length**2*pi
#         elif self.kindShape == "square":
#             return self.length**2
#         elif self.kindShape == 'triangle':
#             return self.length**2 * sqrt(3) / 4
#     def Perimeter(self):
#         if self.kindShape == 'circle':
#             return self.length*2*pi
#         elif self.kindShape == "square":
#             return self.length*4
#         elif self.kindShape == 'triangle':
#             return self.length*3
# p1 = Shape('triangle',10)
# print(p1.Area()) 
# print(p1.Perimeter())
#5
# class binaryTree():
#     def __init__(self,) -> None:
# =
# ?
#6
# class stackStructure():
#     def __init__(self,data) -> None:
#         self.data = data
#     def showValues(self):
#         return self.data
#     def insertValue(self,ins):
#         self.data.append(ins)
#     def popValue(self,inx):
#         self.data.pop(inx)
# p1 = stackStructure([2,3,4,5])
# p1.insertValue(6)
# p1.popValue(4)
# print(p1.showValues())
#7
# class Node():
#     def __init__(self,data) -> None:
#         self.data = data
#         self.next = None
# class linkedList():
#     def __init__(self):
#         self.head = None
#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" ")
#             current = current.next
#         print()
#     def delete(self, data):
#         if not self.head:
#             return

#         if self.head.data == data:
#             self.head = self.head.next
#             return
# #8
# class Price():
    
#     def __init__(self,item) -> None:
#         self.item = item
#     def itemPrice(self):
#         itemDict = {
#         'milk':100,
#         'coffee':120,
#         'bread':80,
#         'tommato' : 60,
#         'pottato':90,
#         'box' : 10,
#         'gum':5,
#         'oil':130,
#         'sweets':70
#     }
#         return itemDict[self.item]
# class shopingCart():
#     def __init__(self,data) -> None:
#         self.data = data
#     def showCart(self):
#         return self.data
#     def addItem(self,itemName):
#         self.data.append(itemName)
#     def delItem(self,itemName):
#         self.data.remove(itemName)
#     def totalPrice(self):
#         return sum([Price(i).itemPrice() for i in self.data])
# p1 = shopingCart(['milk','box'])
# p1.addItem('box')
# p1.delItem('milk')
# print(p1.showCart())
# print(p1.totalPrice())
#9 alredy finished 7
#10 TO Do

#1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              1                              
# class Bank():
#     def __init__(self) -> None:
#         self.allCustomers = {}
# class bankAccount(Bank):
#     def __init__(self,status,customer) -> None:
#         self.status = status
#         self.customer = customer
#         self.allCustomers[customer] = status
#     def showStatus(self):
#         return self.status
#     def transaction(self,transMode,transValue):
#         if transMode == 'a':
#             self.status += transValue
#         elif transMode == 'e':
#             self.status -= transValue
        





        



        

        


        
    