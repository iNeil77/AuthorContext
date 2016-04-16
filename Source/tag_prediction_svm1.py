#### SVM CLASSIFICATION ####

from sklearn import svm


weight10000=open('IRE/weight10000.txt',encoding="utf8").readlines()
tags10000=open('IRE/tags10000.txt',encoding="utf8").readlines()
print(int(tags10000[9999]))
tags=[]
for i in range(0,len(tags10000)):
    temp=tags10000[i]
    temp=int(temp)
    tags.append(temp)
weights=[]
for i in range(0,len(weight10000)):
    temp=weight10000[i].replace('\n','')
    temp=temp.strip()
    temp=temp.split(' ')
    temp=[float(j) for j in temp]
    weights.append(temp)