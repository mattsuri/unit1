#Matthew Suriawinata
#1/24/18
#binaryBackwards.py - base number to binary number


baseNumber = int(input("Input a number to be converted into binary; ")

eighthsDigit = baseNumber//(2**8)
seventhsDigit = (baseNumber - (eighthsDigit * 2**8))//2**7
sixthsDigit - (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7))//2**6)
fifthsDigit - (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6)//2**5)
fourthsDigit - (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6) - (fifthsDigit * 2**5)//2**4)
thridsDigit - (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6) - (fifthsDigit * 2**5) - (fourthsDigit * 2**4) //2**3)
secondsDigit = (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6) - (fifthsDigit * 2**5) - (fourthDigit * 2**4) - (thridsDigit * 2**3) //2**2)
firstsDigit = (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6) - (fifthsDigit * 2**5) - (fourthsDigit * 2**4) - (thridsDigit * 2**3) -(secondsDigit * 2**2) //2**1)
zerosDigit = (baseNumber - (eighthsDigit * 2**8) - (seventhsDigit * 2**7) -(sixthxDigit * 2**6) - (fifthsDigit * 2**5) - (fourthsDigit * 2**4) - (thridsDigit * 2**3) -(secondsDigit * 2**2) - (firstsDigit * 2**1)  //2**0)

print(eightsDigit, sevethsDigit 