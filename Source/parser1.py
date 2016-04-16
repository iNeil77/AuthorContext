####### Matching paper names from DBLP dataset from arnetminer.org and Previous Dataset used in reference paper #######


import sys
from imp import reload
import re

# reload(sys)  
# sys.setdefaultencoding('utf8')
papers1 = open("IRE/CD_merge_result_dec_17_red.txt",encoding="utf8").readlines()
print(len(papers1))
s=papers1[4]

print(s.split("\t"))

for i in range(0,len(papers1)):
    s=papers1[i]
    temp=s.split("\t")
    string = re.sub(r'\W+', '', temp[0].lower())
    papers1[i]=string
    
papers2=[]

temp_papers2 = open("IRE/acm_output.txt", encoding="utf8").readlines()
print(len(temp_papers2))
print(temp_papers2[1])
p= re.compile('#\*(.*)')

for i in range(0,len(temp_papers2)):
    s=p.findall(temp_papers2[i])
    if(s!=[]):
        string=s[0]
        string=re.sub(r'\W+', '', string.lower())
        #s=s.rstrip('.')
        papers2.append(string)
		
		
		
		
		  
papers1 = open("IRE/CD_merge_result_dec_17_red.txt",encoding="utf8").readlines()


for i in range(0,len(papers1)):
    s=papers1[i]
    temp=s.split("\t")
    temp[0] = re.sub(r'\W+', '', temp[0].lower())
    temp=itemgetter(0,-2)(temp)
    papers1[i]=temp
    
papers2=[]

temp_papers2 = open("IRE/acm_output.txt", encoding="utf8").readlines()
p= re.compile('#\*(.*)')
p2= re.compile('#@(.*)')
p3= re.compile('#arnet(.*)')
f_string=''

for i in range(0,len(temp_papers2)):
    s=p.findall(temp_papers2[i])
    if(s!=[]):
        string=s[0]
        string=re.sub(r'\W+', '', string.lower())
        f_string=string
        
    s2=p2.findall(temp_papers2[i])
    if(s2!=[]):
        string2=s2[0]
        f_string=f_string+'\t'+string2
        
    s3=p3.findall(temp_papers2[i])
    if(s3!=[]):
        string3=s3[0]
        f_string=f_string+'\t'+string3
        papers2.append(f_string.split('\t'))
        f_string=''

papers1.sort(key=lambda x: x[0])
papers2.sort(key=lambda x: x[0])

lines = ''
i=0
for row in papers1:
    lines=str(row[0])+'\t'+str(row[1])
    papers1[i]=str(lines)
    i=i+1
    lines=''
    
lines = ''
i=0
for row in papers2:
    lines=str(row[0])+'\t'+str(row[1])+'\t'+str(row[2])
    papers2[i]=str(lines)
    i=i+1
    lines=''
    
f = open('IRE/papers2.txt', 'w',encoding="utf8")
f.write("\n".join(papers2))
f.close()