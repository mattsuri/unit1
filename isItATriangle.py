#Matthew Suriawinata
#1/19/18
#isItATriangle.py - Whether a the shape is a triangle

sideA = float(input("Enter Side A: "))
sideB = float(input("Enter Side B: "))
sideC = float(input("Enter Side C: "))

hyp = max(sideA, sideB, sideC)
leg1 = min(sideA, sideB, sideC)


perimeter = sideA + sideB + sideC
leg2 = perimeter - hpy - leg1

print(leg1 + leg2 > hpy)



