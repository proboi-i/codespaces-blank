import autocorrect as ac
import time
def remove_punctuation_parser(text):
    """Internal Function to remove punctuation and split the text into a list of words"""
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punctuation:
            text = text.replace(i, " ")
    text = text.lower()
    text = " ".join(text.split())
    return  text.split(" ")
#isword() works as expected
#calculate the time it takes to run the code

# ["zwiebac", "brother", "arie", "hello", "h","he","hel","hell",]
text = "hey therer"
start = time.time()
text = remove_punctuation_parser(text)
for i in text:
    try:
        print(ac.autocorrect(i)[0])
    except:
        print(ac.autocorrect(i))
#program runs as expected
end = time.time()
print(end-start)