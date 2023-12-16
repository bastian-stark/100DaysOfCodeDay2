#Tip Calculator App

#Intro
print('Welcome to the tip calculator.')
#Inputs
total_bill = float(input('What was the total bill? $'))
num_people = float(input('How many people to split the bill?\n'))
percentage_tip = float(input('What percentage tip would you like to give? 10, 12, or 15?\n'))
#Calculate tip
total_afterTax = total_bill * (1 + (percentage_tip / 100))
bill = round(total_afterTax / num_people, 2)
print(f'Each person should pay: $ {bill}')
