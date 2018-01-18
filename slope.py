#Matthew Suriawinata    
#1/18/18
#slope.py - slopes

x1 = int(input("x1 = "))

y1 = int(input("y1 = "))

x2 = int(input("x2 ="))

y2 = int(input("y2 ="))

slope = (y1 - y2 )/(x1 - x2)

yintercept = y1 - (slope * x1) 

print("Your slope is ", slope)
print("Your equation is y = ", slope, "x +", yintercept)