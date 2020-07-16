import math
def log(n,ex):
    return ex * math.log(n)
def check_wheather(n1,ex1,n2,ex2):
    if ( log(n1,ex1) > log(n2,ex2)):print("{}^{} is greater".format(n1,ex1))
    elif (log(n1,ex1) < log(n2,ex2)):print("{}^{} is greater".format(n2,ex2))
    else:print("Both are equal.");
t = int(input())
for _ in range(0,t):
    n1,ex1,n2,ex2=map(int,input().split())
    check_wheather(n1,ex1,n2,ex2)