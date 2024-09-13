a = open('input.txt','r')
b = open('output.txt','w')
numb = a.readline()
s = a.readline()
numb = numb.split()
numb = list(map(int,numb))
summ=0
pr=1
if s == '+':
    for i in range(len(numb)):
        summ=summ+numb[i]
    b.write(str(summ))
elif s == '-':
    diff = numb[0]
    for i in range(1,len(numb),1):
        diff=diff+(numb[i]*(-1))
    b.write(str(diff))
else:
    for i in range(len(numb)):
        pr=pr*numb[i]
    b.write(str(pr))
b.close()


