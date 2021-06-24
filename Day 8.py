# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
d={}
for _ in range(int(n)):
    nm,phn=input().split()
    d[nm]=phn

while True:
    try:
        inp=input()
        if inp in d.keys():
            print(inp+"="+d[inp])
        else:
            print("Not found")
    except EOFError:
        break 

