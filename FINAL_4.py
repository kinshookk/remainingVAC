n=int(input())
tec=n
name=[]
marks=[]
while n:
    s,a=input().split()
    a=int(a)
    n-=1
    if not name and not marks:
        name.append(s)
        marks.append(a)
    else:
        marks.append(a)
        marks.sort(reverse=True)
        indexx=marks.index(a)
        name.insert(indexx,s)

dicttt={marks[i]:[] for i in range(tec)}
for i in range(tec):
    dicttt[marks[i]].append(name[i])
for i in range(tec):
    dicttt[marks[i]].sort(reverse=True)
keyer=list(dicttt.keys())
for i in range(len(keyer)):
    for j in range(len(dicttt[marks[i]])):
        print(f"{dicttt[marks[i]][j]} {keyer[i]}")


