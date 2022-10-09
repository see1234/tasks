my_input = list(map(int,list(input())))
minposone=9
minpostwo=9
j=0
for i in my_input:
    if minposone > int(i):
        minposone=j
    j+=1
j=0
for i in my_input:
    if minpostwo > int(i) and not minposone == j:
        minpostwo=j
    j+=1
my_input[minposone], my_input[minpostwo] = -1, -1
result=''
for i in my_input:
    if i != -1:
        result+=str(i)
print(result)