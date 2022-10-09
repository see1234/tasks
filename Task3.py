from math import *

my_input=int(input())
if str(my_input)[len(str(my_input))-1] != '5':
    print('че это')
elif pow(4*10,5) <= my_input:
    print('че это')
else:
    numberA=int('0'+str(my_input)[:-1])+0
    numberB=int('0'+str(my_input)[:-1])+1
    if numberA*numberB == 0:
        print('25')
    else:
        print(str(numberA*numberB)+'25')
# рофл но почему то не скомпилилось
#from math import *

#my_input=int(input())
#print(my_input*my_input) самое тупое решение которое можно придумать...