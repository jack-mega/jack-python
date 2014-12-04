n = raw_input('n,k= (1<=n<=20, 1<=k<=5)')
k = raw_input()
        
t = 1
for i in range(int(k)):
    t = t * int(n)
    
s = 0
for i in range(1, t+1):
    if t % i == 0:
        s += i
        
print s

