##### List the unique tags from the dataset for the learned weight vectors. The tags will act as labels #####

uniq_final_tags = open('IRE/uniq_final_tags.txt', encoding="utf8").readlines()
uniq_tags=[]
key=0
for i in range(0,len(uniq_final_tags)):
    temp1=uniq_final_tags[i].split('\t')
    temp1=str(temp1[1])
    uniq_tags.append(temp1)
    key+=1
    
uniq_tags=list(set(uniq_tags))

mappings=open('IRE/finalrandommappings10000.txt',encoding="utf8").readlines()
uniq_final_tags=open('IRE/uniq_final_tags.txt',encoding="utf8").readlines()
uniq_final_tags2=[]
for i in range(0,len(uniq_final_tags)):
    temp0=uniq_final_tags[i].split('\t')
    temp1=temp0[1]
    temp0=temp0[0]
    
    for j in range(0,len(uniq_tags)):
        temp2=uniq_tags[j].split('\t')
        temp3=temp2[1]
        temp2=temp2[0]
        uniq_final_tags[i]=uniq_final_tags[i].replace(temp2,temp3)
            
print((uniq_final_tags[8999]))
tags10000=[]
mappingsd={}
for i in range(0,len(uniq_final_tags)):
    temp=uniq_final_tags[i].replace('\n','')
    temp=uniq_final_tags[i].split('\t')
    #temp = re.sub("\d+", "", temp)
    mappingsd[str(temp[0])]=temp[1]
    for j in range(0,len(uniq_final_tags)):
        temp0=uniq_final_tags[i].split('\t')
        temp1=temp0[1]
        temp0=temp0[0]
        if(temp==temp0):
            tags10000.append(temp1)

for i in range(0,len(mappings)):
    temp=mappings[i].replace('\n','')
    temp=re.sub("\d+", "",temp)
    temp=temp.strip()
    key=mappingsd[str(temp)]
    tags10000.append(key)
            
for i in range(0,len(uniq_final_tags)):
    uniq_final_tags[i]=uniq_final_tags[i].replace('\n','')
	
	

f = open('IRE/tags10000.txt', 'w',encoding="utf8")
f.write("\n".join(tags10000))
f.close()