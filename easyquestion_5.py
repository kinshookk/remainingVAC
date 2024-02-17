def primeprinter(n):
    ans=[]
    for i in range(2,n+1):
        flag=True
        for j in range(2,i):
            if i%j==0:
                flag=False
        if(flag):
            ans.append(i)
    print(*ans)
def main():
    n=int(input())
    primeprinter(n)
if __name__=='__main__':
    main()
