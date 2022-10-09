#A+B
from math import pow
my_input=input()
res=0
for i in str(my_input).split():
    if pow(10,9) > int(i) and int(i) > 0:
        res+=int(i)
print(res)