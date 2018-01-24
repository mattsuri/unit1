#Matthew Suriawinata
#1/24/18
#binary.py - converts binary to base ten

binaryNumber = int(input("Enter an 8 digit binary number: "))

first = (binaryNumber%10)
second = (binaryNumber//10)%10
thrid = (binaryNumber//100)%10
fourth = (binaryNumber//1000)%10
fifth = (binaryNumber//10000)%10
sixth = (binaryNumber//100000)%10
seventh = (binaryNumber//1000000)%10
eighth = (binaryNumber//1000000)%10

decimalNumber = ((first*2**0) + (second*2**1) + (thrid*2**2) + (fourth*2**3) + 
                (fifth*2**4) + (sixth*2**5) + (seventh*2**6) + (eighth*2**7))


print(decimalNumber)