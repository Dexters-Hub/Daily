def xyz(a):
    y=a
    x=[0]*len(a)
    count =0

    while(x!=a):
        count+=1
        x=[0]*len(a)
        for i in range(len(a)):
            x[a[i]-1] = y[i]
        y=x
    return (count)

T= int(input())
for _ in range(T):
    n= int(input())
    monkeys = list(map(int,input().split()))
    result = xyz(monkeys)
    print(result)

