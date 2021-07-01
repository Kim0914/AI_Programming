n,k = input().split()
n = int(n)
k = int(k)

count = 0
for div in range(n+1):
    if(div > 0):
        if(n%div == 0):
            count += 1
            if(count == k):
                print(div)
if(count < k):
    print(0)