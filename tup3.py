promp = input('Enter a file:')
try:
    fhandle = open(promp)

except:
    print('No file found!')
    quit()


dic = dict()
for index in fhandle:
    words = index.split()

    for val in words:
        dic[val] = dic.get(val,0) + 1
lst = list()

for k,v in dic.items():
    tups = (v,k)
    lst.append(tups)

lst = sorted(lst,reverse=True)

for value,key in lst[:10]:
    print(key,value)
