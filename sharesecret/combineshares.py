import words
import sys

M=7759

def eliminate(A):
    for i in range(len(A)):
        j=i
        while A[j][i]==0:
            j=j+1
        A[i],A[j]=A[j],A[i]
        b=(A[i][i]**(M-2))%M
        A[i]=[(a*b)%M for a in A[i]]

        for j in range(len(A)):
            if j!=i:
                m=-A[j][i]
                for k in range(len(A[0])):
                    A[j][k]=(A[j][k]+m*A[i][k])%M
            
def solveproblem(P):
    X=[]
    for x in P.keys():
        X1=[]
        for i in range(len(P.keys())):
            X1.append((x**i)%M)
        X1.append(P[x])
        X.append(X1)
    eliminate(X)
    return X[0][-1]

print 'Enter your shares, one per line.  Finish with "end".'
print 'Be sure to include the number at the start of each share.'
print 

d=[]

while True:
    s=raw_input()
    if s=="end":
        break
    s=s.split()
    x=int(s[0])
    s=s[1:]
    for i in range(len(s)):
        if len(d)<i+1:
            d.append({})
        d[i][x]=words.word2num[s[i]]

print
print "The pass-phrase is:"
for P in d:
    print words.num2word[int(solveproblem(P))],
print
