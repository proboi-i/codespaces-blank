import json 
def negative(word):
    with open(".github_materials/negative.json") as f:
        negative = json.load(f)
        start = word[0]
        for i in negative[start]:
            if i == word:
                return 0
        else: 
            return 3
def positive(word):
    with open(".github_materials/positive.json") as f:
        positive = json.load(f)
        start = word[0]
        for i in positive[start]:
            if i == word:
                return 1
        else: 
            return 3