
fileName = input("enter your file name")
file=open(fileName, 'r')
wordcount={}
for word in file.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in wordcount.items():
    print (k, v)