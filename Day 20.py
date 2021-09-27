# a=[4,3,1,2]
a=[3,2,1]
# a=[1,2,3]
swaps=0
for i in range(len(a)):
#     swaps=0
    for j in range(len(a)-1):
        if a[j]>a[j+1]:
            a[j],a[j+1]=a[j+1],a[j]
            swaps+=1
            print(a)
print(swaps)