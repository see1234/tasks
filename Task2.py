from math import pow
i=int(input())
res=0
if pow(10, 4) > i:
    if i > 0:
        res=sum(range(1,i+1))
    else:
        res=-sum(range(-1,abs(i)+1))
print(res)