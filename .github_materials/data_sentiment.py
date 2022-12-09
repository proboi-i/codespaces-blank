
#@-- path /workspaces/nlp_analysis/.github_materials/data_sentiment.py-- @

#this is a script to get the sentiment of the data
import files as fl 
#create aoo time function to calculate the time it takes to run the script
text = "Happy to be with you "
print(text)
#create a function to remove the punctuation and seperate the words
def remove_punctuation(text):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punctuation:
            text = text.replace(i, " ")
    text = text.lower()
    text = " ".join(text.split())
    return text
#call the function
text = remove_punctuation(text)
text = text.split(" ")
num = [] 
for i in  text:
    if fl.positive(i) == 1:
        num.append(1)
    elif fl.negative(i) == 0:
        num.append(0)
    else:
        num.append(3)
print(num)
#create a function to find the percentange of positive and negative words
def sentiment(num):
    pos = 0
    neg = 0
    for i in num:
        if i == 1:
            pos += 1
        elif i == 0:
            neg += 1
    return pos, neg
#call the function
pos, neg = sentiment(num)
print(pos, neg)
#calculate the percentage of positive and negative words
total = len(num)
pos = (pos/total)*100
neg = (neg/total)*100
print(pos, neg)
#probability of the data being positive or negative

if pos > neg:
    pos = pos+neg #a bias that shows that the negative word is sarcastic and has no effect on the outcome sentiment of the text
    print("The data is positive",pos,"%")
elif neg > pos:
    neg = pos+neg #a bias that shows that the positive word is sarcastic and has no effect on the outcome sentiment of the text 
    print("The data is negative",neg,"%") 
    for i in range(len(num)): 
        if num[i] == 1:
           print("The '%s' word is positive but sarcastic"%text[i])
        elif num[i] == 0:
            print("The '%s' word is negative "%text[i])
else:
    print("The data is neutral")
    print("equal positive and negative words")# a problem with this is that it does not take into account the number of words in the text
    #this is to solved later on
#to produce what is likely to be used in a sentiment of the text 
#if we use a positive word in a negative sentce it is likely to be sarcastic and negative similar to the example above
#we can use this to find the sentiment of the text
