word2num={}
num2word={}

i=0
for x in open("eff_large_wordlist.txt").readlines():
    w=x.split()[1]
    word2num[w]=i
    num2word[i]=w
    i=i+1
    
    
