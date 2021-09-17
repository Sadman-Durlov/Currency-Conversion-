k=1
s=0
a = input('Type no. of iterations: ')
b= int (a)
for x in range(b):
    if x%2==0:
        s+=4/k
    else:
        s-=4/k

    k+=2
    print(s)
