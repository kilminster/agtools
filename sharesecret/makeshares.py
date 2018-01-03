import sys
import words
import rng

M=7759

length=int(sys.argv[1])
order=int(sys.argv[2])
number=int(sys.argv[3])

polys=[]
for i in range(length):
    poly=[]
    for j in range(order):
        poly.append(rng.random_int(M))
        print i,j
    polys.append(poly)

def evalpoly(poly,x):
    r=0
    for i in range(len(poly)):
        r=(r+poly[i]*(x**i))%M
    return r

for x in range(1,number+1):
    print x,
    for p in polys:
        print words.num2word[int(evalpoly(p,x))],
    print

print "--------------------------------------------"
for p in polys:
    print words.num2word[int(evalpoly(p,0))],
print


