#Tip Calculator

print('Welcome to the tip caalculator.')
bill = float(input('What was the total  bill? $'))
per = int(input('What prcentage tip would you like to give?10, 12 or 15?'))
people = int(input('How many people to split the bill?'))
total = bill/people + (bill/people)*per/100
print('Each person should pay: $', round(total,2))