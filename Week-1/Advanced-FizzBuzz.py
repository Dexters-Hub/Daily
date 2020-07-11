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
        print("Error")

def fizzbuzz(num, keymap):
    output = ''
    for factor in keymap.keys():
        if(num % factor == 0):
            output += keymap[factor]
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