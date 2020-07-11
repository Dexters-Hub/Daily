def numbers(n):
    C = input().split()
    try:
        if len(C) == n:
            values = [int(x) for x in C]
        return values
    except:
        print("UnboundLocalError")
        
    
def text(n):
    word = input().split()
    try:
        if len(word) == n:
            return word
    except:
        print("UnboundLocalError")

def fizzbuzz(num, keymap):
    output = ''
    for _ in keymap.keys():
        if(num % _ == 0):
            output += keymap[_]
    if(not output):
        output = num
    return output


cycles = 100
N = int(input())

values = numbers(N)

words = text(N)

conditions = dict(zip(values, words))

for num in range(1, cycles+1):
    print(fizzbuzz(num, conditions))