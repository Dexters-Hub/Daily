N= int(input())
br_arr=input()
gr_arr = input()
gr =0
gm =0
for g in gr_arr:
    if(g=='r'):
        gr+=1
    else:
        gm+=1

count =0

for b in br_arr:
    if(b=='r'):
        if(gr>0):
            gr-=1
            count+=1
        else:
            break
    else:
        if(gm>0):
            gm-=1
            count+=1
        else:
            break
print(N-count)