from collections import Counter
from nltk import FreqDist, word_tokenize
import nltk
import re
f=open('t3.txt','r')
text=f.read()
trackid=[]
cardinal=[]
alpha=[]
alphanum=[]
lines=((text).upper().split('\n'))
for i in lines:
    wt=word_tokenize(i)
    words=(nltk.pos_tag(wt))
    for j in range(0,len(words)):
        if(words[j][1]=='CD'):
            cardinal.append(words[j][0])
        elif(re.match("^[a-zA-Z0-9]+(?:_[a-zA-Z0-9]+)?$", words[j][0])):
            alphanum.append(words[j][0])
        if(words[j][0].isalpha()):
            alpha.append(words[j][0])
test=set(alphanum)-set(alpha)
trackid=list(set().union(test,cardinal))
trackid8=[]
for i in trackid:
    if(len(i)>8):
        trackid8.append(i)
#print(trackid8)
validation=["^[L][A-Z][0-9]{9}[D][E]$","^[R][A-Z][0-9]{9}[D][E]$","^[C][N][A]{2}[H][0-9]{9}$","^[S][G][K][E][N]{10}$","^[G][M][0-9]{16}$","^[G][M][0-9]{17}$"
,"^[G][M][0-9]{18}$"
,"^[A][A-Z][0-9][0]{3}[0-9]{15}$"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[L][A-Z][0-9]{9}[D][E] $"
,"^[J]{2}[D][0-9]{13}$"
,"^[J]{2}[D][0-9]{18}$"
,"^[A][A-Z][0-9]{9}[E][S]$"
,"^[C][A-Z][0-9]{9}[E][S]$"
,"^[E][A-Z][0-9]{9}[E][S]$"
,"^[L][A-Z][0-9]{9}[E][S]$"
,"^[R][A-Z][0-9]{9}[E][S]$"
,"^[S][A-Z][0-9]{9}[E][S]$"
,"^[V][A-Z][0-9]{9}[E][S]$"
,"^[C][D][0-9]{11}$"
,"^[C][U][0-9]{11}$"
,"^[G][I][0-9]{10}$"
,"^[P][A][0-9]{10}$"
,"^[V][D][0-9]{10}$"
,"^[C][D][0-9]{21}$"
,"^[C][U][0-9]{21}$"
,"^[G][I][0-9]{21}$"
,"^[P][A][0-9]{21}$"
,"^[V][D][0-9]{21}$"
,"^[A][A-Z][0-9]{9}[G][B]$"
,"^[B][A-Z][0-9]{9}[G][B]$’"
,"^[F][A-Z][0-9]{9}[G][B]$’"
,"^[J][A-Z][0-9]{9}[G][B]$’"
,"^[K][A-Z][0-9]{9}[G][B]$’"
,"^[L][A-Z][0-9]{9}[G][B]$’"
,"^[Q][A-Z][0-9]{9}[G][B]$’"
,"^[R][A-Z][0-9]{9}[G][B]$’"
,"^[S][A-Z][0-9]{9}[G][B]$’"
,"^[V][A-Z][0-9]{9}[G][B]$"
,"^[W][A-Z][0-9]{9}[G][B]$"
,"^[X][A-Z][0-9]{9}[G][B]$"
,"^[Y][A-Z][0-9]{9}[G][B]$"
,"^[Z][A-Z][0-9]{9}[G][B]$"
,"^[C][A-Z][0-9]{9}[G][B]$"
,"^[E][A-Z][0-9]{9}[G][B]$"
,"^[A-Z]{4}[0-9]{7}[G][B]$"
,"^[P][A-Z]{3}[0-9]{7}$"
,"^[A][H][0-9]{7}$"
,"^[M][L][0-9]{7}$"
,"^[T][F][0-9]{7}$"
,"^[T][G][0-9]{7}$"
,"^[T][Y][0-9]{7}$"
,"^[U][D][0-9]{7}$"
,"^[U][F][0-9]{7}$"
,"^[U][G][0-9]{7}$"
,"^[U][H][0-9]{7}$"
,"^[A][A-Z][0-9]{9}[U][S]$"
,"^[C][A-Z][0-9]{9}[U][S]$"
,"^[D][A-Z][0-9]{9}[U][S]$"
,"^[E][A-Z][0-9]{9}[U][S]$"
,"^[G][A-Z][0-9]{9}[U][S]$"
,"^[L][A-Z][0-9]{9}[U][S]$"
,"^[R][A-Z][0-9]{9}[U][S]$"
,"^[S][A-Z][0-9]{9}[U][S]$"
,"^[T][A-Z][0-9]{9}[U][S]$"
,"^[U][A-Z][0-9]{9}[U][S]$"
,"^[V][A-Z][0-9]{9}[U][S]$’"
,"^[M][0-9]{9}$’"
,"^[M][0-9]{10}$"
,"^[A][A-Z][0-9]{9}[I][T]$"
,"^[C][A-Z][0-9]{9}[I][T]$"
,"^[E][A-Z][0-9]{9}[I][T]$"
,"^[H][A-Z][0-9]{9}[I][T]$"
,"^[K][A-Z][0-9]{9}[I][T]$"
,"^[L][A-Z][0-9]{9}[I][T]$"
,"^[R][A-Z][0-9]{9}[I][T]$"
,"^[S][A-Z][0-9]{9}[I][T]$"
,"^[V][A-Z][0-9]{9}[I][T]$"
,"^[X][A-Z][0-9]{9}[I][T]$"
,"^[Z][A-Z][0-9]{9}[I][T]$"
,"^[H][0-9]{10}$"
,"^[V][0-9]{10}$"
,"^[0-9]{12}[G][L][S]$"
,"^[A][A-Z][0-9]{9}[C][A]$"
,"^[C][A-Z][0-9]{9}[C][A]$"
,"^[E][A-Z][0-9]{9}[C][A]$"
,"^[G][A-Z][0-9]{9}[C][A]$"
,"^[L][A-Z][0-9]{9}[C][A]$"
,"^[1][Z][A-Z][0-9]{9}[0-9]{7}$"
,"^[0-9]{3}[A-Z][0-9]{5}$"]
validid=[]
for i in trackid8:
    for j in validation:
        if(re.match(j,i)):
            validid.append(i)    
print(validid)

        
    
    
    
