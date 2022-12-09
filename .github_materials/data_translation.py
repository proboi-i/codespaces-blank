import json
with open('.github_materials/data.json') as f:
    data = json.load(f)
#function to link words with emotions
def emotion_linker(dict):
    emotion = dict["emotion"]
    words = dict["text"]
    some_simple_nonaction_words = ["i","am","you","there","are","he","she","it","we","they","is","was","were","be","been","being","have","has","had","do","does","did","can","could","may","might","must","shall","should","will","would","a","an","the","and","or","if","then","else","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now","car","bike","dumble","tint","return","dont","iam","theres","didnt"]
    lst = []
    for i in words:
        if i in some_simple_nonaction_words:
            continue
        else:
            link = {}
            print(words)
            print(emotion)
            print('"',i,'"', end=" ")
            a = input("is related to the emotion: ==")
            print(end="\n")
            print()
            if a == "":
                link[emotion] = i
                lst.append(link)
                print(lst)
            else:
                print("no.")
                some_simple_nonaction_words.append(i)
                continue
    print(lst)
    print("done")
    return lst
deb_data = []
for i in data:
    deb_data.append(emotion_linker(i))
print("made the list")
with open(".github_materials/deb_data.json", "w") as f:
    json.dump(deb_data, f)
print("done")
