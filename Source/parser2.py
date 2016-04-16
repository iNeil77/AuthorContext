import sys
import os
import random
import re

fname1 = "papers_final.txt"
fname2 = "mappings.txt"
fname3 = "finalmappings.txt"
fname4 = "context.txt"
authorid = 0
authordict = {}
prev = ""
vector = [None]*3
n = 0
with open(fname1, "rt", encoding="utf-8") as f1, open(fname2, "a+", encoding="utf-8") as f2, open(fname3, "a+", encoding="utf-8") as f3, open(fname4, "a+", encoding="utf-8") as f4:
    for line in f1:
        linemod = re.split(r'\t+', line.strip())[1]
        if linemod != "":
            modlinemod = linemod.split(',')
            for author in modlinemod:
                print(author.strip(), file = f2)
    f2.flush()
    os.fsync(f2.fileno())
    f2.seek(0, 0)
    refer = f2.readlines()
    refer.sort()
    for line in refer:
        if line != prev:
            authordict[line.strip()] = authorid
            print(line.strip()+" "+str(authorid), file=f3)
            authorid = authorid + 1
        prev = line
    f3.flush()
    os.fsync(f3.fileno())
    f3.seek(0, 0)
    f1.flush()
    os.fsync(f1.fileno())
    f1.seek(0, 0)
    for line in f1:
        linemod = re.split(r'\t+', line.strip())[1]
        if linemod != "":
            modlinemod = linemod.split(',')
            for i in range(0,len(modlinemod)):
                modlinemod[i] = modlinemod[i].strip()
            for i in range(0,len(modlinemod)):
                for j in range(i+1,len(modlinemod)):
                    vector = [None]*3
                    vector[0] = authordict[modlinemod[i].strip()]
                    vector[1] = authordict[modlinemod[j].strip()]
                    k = 0
                    while k < 3:
                        neg = random.choice(refer)
                        if neg.strip() in modlinemod:
                            continue
                        vector[2] = authordict[neg.strip()]
                        k = k + 1
                        print(str(vector[0])+","+str(vector[1])+","+str(vector[2]), file=f4)
                        print(n)
                        n = n + 1

print(authorid)
print(len(authordict))
