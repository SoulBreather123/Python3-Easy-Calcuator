
import random



listContent1 = ["1) Addition", "2) Subtraction", "3) Multiplication", "4) Dividing",
"5) Random Number Generator (1-100)"]

releaseIsset1 = {"v0"}
releaseIsset1.update("v2","congs")

print(listContent1[0])
print(listContent1[1])
print(listContent1[2])
print(listContent1[3])
print(listContent1[4])










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

if selectOne == 5:
    print("Random Number is:", random.randrange(1, 100))











