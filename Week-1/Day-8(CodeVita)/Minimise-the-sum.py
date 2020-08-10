N, K= int(input()).split()
o_array = list(map(int, input().split(' ')[:N]))

for i in range(int(K)):
    maximum = max(o_array)
    o_array.remove(maximum)
    o_array.append(maximum//2)
print(sum(o_array))