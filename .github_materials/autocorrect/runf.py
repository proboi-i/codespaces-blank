import pickle as pkl
import json 
data_set = pkl.load(open('.github_materials/autocorrect/bin.dat', 'rb')) 
#create a dictionart with all characters AS keys
a = {} 
singles = []
for i in range(97, 123):
    a[chr(i)] = {}
    for j in range(97, 123):
        a[chr(i)][chr(i)+chr(j)] = {}
        for k in range(97, 123):    
            a[chr(i)][chr(i)+chr(j)][chr(i)+chr(j)+chr(k)] = []
for i in data_set.keys():
    try:
        if len(i)>3:
            a[i[0]][i[0]+i[1]][i[0]+i[1]+i[2]].append(i)
        elif len(i) ==2:
            a[i[0]][i[0]+i[1]].append(i)
    except:
        singles.append(i)
with open('.github_materials/autocorrect/txr.bat', 'wb') as f:
    pkl.dump(a, f)