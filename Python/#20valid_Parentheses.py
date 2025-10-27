s="(){}}{"
brackets=['(',')','[',']','{','}']
l1=len(s)
t=l1
l=len(brackets)
k=0
for i in range(l1-1):
    t=t-1
    for j in range(l):
        if s[i]==brackets[j] and j%2==0:
            if s[i+1] == brackets[j+1] or s[t] == brackets[j+1]:
                print("si", s[i+1])
                print("st", s[t])
                print("b", brackets[j+1])
                k=k+1
            else:
                k=-1
                break
if k==0:
    print('false')
else:
    print(k)
    print('true')
            
