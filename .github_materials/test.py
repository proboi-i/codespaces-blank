import json
import pickle
with open("/workspaces/codespaces-blank/.github_materials/autocorrect/words_dictionary.json","r") as f:
    words = json.load(f)
    lst = [] 
for i in words.keys():
    if len(i) <=3:
        lst.append(i)
a = {} 
for i in range(97,123):
    a[chr(i)] = []
for i in lst:
    a[i[0]].append(i)
with open("/workspaces/codespaces-blank/.github_materials/autocorrect/small.json","w") as f:
    json.dump(a,f)
with open("/workspaces/codespaces-blank/.github_materials/autocorrect/small.dat","wb") as f:
    pickle.dump(a,f)
