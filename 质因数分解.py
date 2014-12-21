n = int(raw_input())


def prime(n):
    f = True
    for i in range (2, int(n ** 0.5)):
        if n % i == 0:
            f = False
            break
    if f == True: return True
    else: return False

l = []
n1 = n

for j in range (2, n1):
    if prime(j) == True:
        while n % j==0:
            n = n / j
            l.insert(0, j)
            print j
            print n
            if n <> 1:
                l.insert(0, '*')

print n1,'=',
t = 0
while l <> []:
    t += 1
    if t % 2 == 1:
        print int(l[0]),
    else:
        print '*',
    del l[0]
    

        
        
        
