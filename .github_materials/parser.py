import csv
import json
import string
#! path /workspaces/nlp_analysis/.github_materials/parser.py
with open('.github_materials/samples.csv', 'r') as f:
    reader = csv.reader(f)
    data = []
    for row in reader:
        data.append(row)

def remove_punctiation(text):
    for p in string.punctuation:
        text = text.replace(p, '')
    return text
print(remove_punctiation("Hello, world!"))
met_data = []
for i in data:
    a = {}
    a["emotion"] = i[1]
    text = remove_punctiation(i[3]).split(" ")
    #remove all the "" from the list named text
    text = [x for x in text if x != '']
    a["text"] = text
    met_data.append(a)
    #create a function to split the text into words 
    #create a function to remove punctuation
with open('/workspaces/nlp_analysis/.github_materials/data_indented.json', 'w',encoding="utf-8") as f:
    json.dump(met_data, f,indent=4)
