#Matthew Suriawinata
#1/19/18
#change.py - converts your change into coins

initialcents = int(input("Number of cents: "))

quarters = int(initialcents/25)
dimes = int((initialcents - (25 *quarters))/10)
nickles = int(initialcents + (-25 * quarters) + (-10 * dimes)/ 5)
pennies = int(initialcents  + (-25 * quarters) + (-10 * dimes) + (-5 * nickles)/ 1)

print("Quarters: ", quarters)
print("Dimes: ", dimes)
print("Nickles: ", nickles)
print("Pennies: ", pennies)