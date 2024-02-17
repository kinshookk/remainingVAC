n=int(input())
first=0
second=1
nth=n
if n==1:
    print(0,end="")
elif n==2:
    print(0,end="")
    print(1)
else:
    print(first,end=" ")
    print(second,end= " ")
    for i in range(2,n):
        nth=first+second
        first=second
        second=nth
        print(nth,end=" ")
    