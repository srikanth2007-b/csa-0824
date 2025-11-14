p=int(input("enter the principel of amount:"))
n=int (input("enter the numberof years;"))
sc=input ("senior citizen yes\no:")
g=input ("mail\female:")
if sc=='y'and g=='m':
    print("si=",(p*n*12)/100)
elif sc=='y'and g=='f':
    print ("sr=",(p*n*15)/100)
else:
    print("sr=",(p*n*10)/100)
    
