################ TAGGING: getting tags of authors from DBLP dataset ##################


from collections import defaultdict
import re
import operator

class AutoVivification(dict):
    """Implementation of perl's autovivification feature."""
    def __getitem__(self, item):
        try:
            return dict.__getitem__(self, item)
        except KeyError:
            value = self[item] = type(self)()
            return value

papers1 = open("IRE/CS_Citation_Network.txt",encoding="utf8").readlines()
p1= re.compile('#@(.*)')
p2= re.compile('#f(.*)')
dic1 = AutoVivification()

for i in range(0,len(papers1)):
    s=p1.findall(papers1[i])
    if(s!=[]):
        string1=s[0]
        string1=string1.split(',')
        
    s=p2.findall(papers1[i])
    if(s!=[]):
        string2=s[0]
        for j in range(0,len(string1)):
            if(dic1[str(string1[j])][string2]!={}):
                dic1[str(string1[j])][string2]+=1
            else:
                dic1[str(string1[j])][string2]=1
string1=''
final_tags=[]
for w in dic1:
    temp1=dic1[w]
    temp1= sorted(temp1.items(), key=operator.itemgetter(1))
    string1=str(w)+'\t'+str(temp1[-1][0])
    final_tags.append(string1)
	
	
f = open('IRE/final_tags.txt', 'w',encoding="utf8")
f.write("\n".join(final_tags))
f.close()
	
	
	
######### Filter duplicate authors and keep only unique authors ###########

import re
p4=re.compile("\d+")
final_tags = open("IRE/final_tags.txt",encoding="utf8").readlines()
print(len(final_tags))
final_tags.sort()
final_tags=final_tags[501056:1002117]
print(len(final_tags))

print(final_tags[0])
papers_final= open("IRE/papers_final.txt",encoding="utf8").readlines()
# print(papers_final[0])
print((temp_authors[0]))

temp_authors=[]
for i in range(0,len(papers_final)):
    temp_authors.append(papers_final[i].split('\t')[1])

uniq_authors={}
string=''
for i in range(0,len(temp_authors)):
    string=temp_authors[i].split(',')
    for j in range(0,len(string)):
         uniq_authors[str(string[j])]=None

uniq_authors=[]
finalmappings= open("IRE/finalmappings.txt",encoding="utf8").readlines()
for i in range(0,len(finalmappings)):
    s=str(finalmappings[i])
    s = p4.sub("", s)
    s=s.replace('\n','')
    uniq_authors.append(s)
	
################## Get Unique final tags ##################



uniq_final_tags=[]
string_final=''
i=0
j=0
count=0
while((i<len(uniq_authors)) & (j<len(final_tags))):
    temp1=uniq_authors[i].strip()
    temp2=final_tags[j]
    temp22=temp2.split('\t')
    temp2=str(temp22[0])
    if(temp1==temp2):
        string_final=temp1+'\t'+str(temp22[1])
        uniq_final_tags.append(string_final)
        string_final=''
        count=count+1
        i=i+1
        j=j+1
    elif(temp1>temp2):
        j=j+1
    elif(temp1<temp2):
        i=i+1

print(len(uniq_final_tags))