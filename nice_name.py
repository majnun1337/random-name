# Nice Name Generator
from random import randint

def randc():
    consonant ="bcdfghjklmnpqrstvwxyz"
    c=randint(0,len(consonant)-1)
    return consonant[c]

def randv():
    vowel = ['a','e','i','o','u','ee','oo']
    v=randint(0,len(vowel)-1)
    return vowel[v]
    
def pattern(vc):
    wrd=""
    for i in vc:
        if i=='v':
            wrd+= randv()
        else:
            wrd+= randc()
    return wrd

def generate(n,LikeThis):
#n = number of random names to generate
#LikeThis = placeholder string like 'vvvccc'; 'v' for vowel and 'c' for consonant; 
    for i in range(n):
        print(pattern(LikeThis))
        
if __name__ == "__main__":

    generate(100,'vcvcv')