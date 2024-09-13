a = list(map(int,input().split()))
srg=1
for i in range(len(a)):
    srg=srg*a[i]
print((srg)**(1/len(a)))