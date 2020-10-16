//WELCOME TO MY CALCUATOR!!
print("1) Addition")
print("2) Subtraction")
print("3) Multiplication")
print("4) Dividing")



selectOne = int(input("Select One:"))
if selectOne == 1:
    xa = int(input("Write First Number: "))
    xaa = int(input("Write Second Number: "))
    resultAddition1 = int(xaa) + int(xa)
    print("Result: ", resultAddition1)

if selectOne == 2:
    xs = int(input("Write First Number: "))
    xss = int(input("Write Second Number: "))
    resultSubtraction1 = int(xs) - int(xss)
    print("Result: ", resultSubtraction1)

if selectOne == 3:
    xm = int(input("Write First Number: "))
    xmm = int(input("Write Second Number: "))
    resultMultiplication = int(xm) * int(xmm)
    print("Result: ", resultMultiplication)

if selectOne == 4:
    xd = int(input("Write First Number: "))
    xdd = int(input("Write Second Number: "))
    resultDividing1 = int(xd) / int(xdd)
    print("Result: ", resultDividing1)



