# This code takes 1 article and returns 

def frequency(wordlist):
    d={}
    for i in wordlist:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d

def mostfreq(flist):
    f_num=0
    f_word="Unable to find title"
    for k in flist:
            if len(k)>4:    # Will try to make this dynamic.
                if int(flist[k])>f_num:
                    f_num=int(flist[k])
                    f_word=k
    return f_word

with open("Files/article1.txt","r") as Ar1:
    Art1 = Ar1.read()

wordlist1=Art1.split()
wordlist1 = [(x.lower()).strip("-,\"\'().") for x in wordlist1]

f1 = frequency(wordlist1)
print(mostfreq(f1))
