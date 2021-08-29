rd=list(map(int,input().split()))
dd=list(map(int,input().split()))
fine=0
yd=rd[2]-dd[2]
md=rd[1]-dd[1]
dyd=rd[0]-dd[0]
if yd>0:
   fine=10000
elif yd==0 and md>0:
    fine=500*md
elif yd==0 and md==0 and dyd>0:
    fine=15*dyd
# res=dyd*15+md*500+yd*10000
print(fine)