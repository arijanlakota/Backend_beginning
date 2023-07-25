#handling expectasions
#1
# try:
#     5 / 0
# except ZeroDivisionError:
#     print("You can't divide with zero")
#2
# try:
#     a = int(input())
#     print(a)
# except ValueError:
#     print("is not a valid integer")
#3
# def findFile(nesto):
#     try:
#         a = open(nesto,'r')
#         print(a)
#         a.close()
#     except FileNotFoundError:
#         print("file do not exist")
# print(findFile("sakdkasjd"))
#4
# def propmtInput(prompt):
#     try:
#         value = float(input(prompt))
#         return value
#     except TypeError:
#         print("no")
# print(propmtInput(5.7))
#5

# def premissionFile(fileName):
#     try:
#         with open(fileName,'w') as file:
#             file.read()
#     except IOError:
#         print("There is a premision error")
# premissionFile("text.txt")
#6
# def handleList(testArr):
#     try:
#         print(testArr[len(testArr)])
#     except IndexError:
#         print("is out of range")
# handleList([1,2,3,4])
#7
# def inputHandle(inp):
#     try:
#         a = input(inp)
#         print(a)
#     except KeyboardInterrupt:
#         print("You press CTRL c")
# n1 = inputHandle("Enter a number: ")
#8
# def myDivide(a,b):
#     try:
#         print(a/b)
#     except ArithmeticError:
#         print("there is an error")
# myDivide(2,2j)
#9
# def unicodeFile(fileName):
#     try:
#         with open(fileName,'r') as file:
#             a = file.read()
#             print(a)
#     except UnicodeDecodeError:
#         print("Something went wrong")
# unicodeFile("text.txt")
#10
# def listAtribute(testArr):
#     try:
#         testArr.nei()
#     except AttributeError:
#         print("nece ona nidje")
# listAtribute([1,2,3,4])





