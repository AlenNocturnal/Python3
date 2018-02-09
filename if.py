x = int(input("Please enter an integer: "))

if x < 0:
   x = 0
   print('Negative changed to zero')
elif x == 0:
   print('Zero')
elif x == 1:
   print('Single')
else:
   print('More')


for i in range(x):
 if x == 3:
    print('Break')
    break
 elif x == 4:
    print('Continue')
    continue
 print(i)
