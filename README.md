# Currency-Conversion-
print('Hello! \n')
print ('Please select currency \n Dollar \n Euro \n')
print('Press the first letter \n')

a = input ()

if (a=='d'):
    print('Enter dollar amount: \n')
    dollar = input()
    bal = float(dollar)*85.27
    print('Balance:',bal)
elif (a=='e'):
    print('Enter euro amount: \n')
    euro = input()
    bal = float(euro)*100.46
    print('Balance:',bal)
else:
    print('No currecy available right now!!!')
