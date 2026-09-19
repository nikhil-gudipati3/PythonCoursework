#type 1
try:
    d={1:1,2:2,3:3}
    print(d[4]) #KeyError
    l=[1,2,3,4,5]
    print(l[6]) #IndexError
    print('a'+12) #TypeError
    b = int(input('Enter a number: ')) #ValueError
    print(n) #NameError
    print(10/0) #ZeroDivisionError
except Exception as e:
    print('Error Occured',e)
else:
    print('No Errors')
finally:
    print('End of program')

#type 2
try:
    d={1:1,2:2,3:3}
    print(d[4]) #KeyError
    l=[1,2,3,4,5]
    print(l[6]) #IndexError
    print('a'+12) #TypeError
    b = int(input('Enter a number: ')) #ValueError
    print(n) #NameError
    print(10/0) #ZeroDivisionError
except (NameError,KeyError,IndexError,TypeError,ValueError,ZeroDivisionError) as e:
    print('Error Occured',e)
else:
    print('No Errors')
finally:
    print('End of program')


#program
try:
    amount = int(input('Enter the amount: '))
    if amount < 0:
        raise Exception('Amount needs to be greater than 0')
except Exception as e:
    print('Error occured',e)
else:
    print('No Errors')
finally:
    print('End of program')
