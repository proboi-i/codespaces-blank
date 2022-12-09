def remove_punctuation_parser(text):
    """Internal Function to remove punctuation and split the text into a list of words"""
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punctuation:
            text = text.replace(i, " ")
    text = text.lower()
    text = " ".join(text.split())
    return  text.split(" ")
#call the function
def remove_punctuation_parser_nolower(text):
    """Internal Function to remove punctuation and split the text into a list of words"""
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for i in text:
        if i in punctuation:
            text = text.replace(i, " ")
    text = " ".join(text.split())
    return  text.split(" ")
def first_person(text):
    word=word2=text
    text = remove_punctuation_parser(text)
    word = remove_punctuation_parser_nolower(word)
    #list of first person pronouns
    first_person_pronouns = ["i", "me", "my", "mine", "we", "us", "our", "ours"]
    for i in range(0,len(text)):
        if text[i] in first_person_pronouns:
            print("The '%s' word is a first person pronoun"%word[i])
    else:
        a = second_person(word2)
        if a == 2:
            print("The data is second person")
        b = third_person(word2)
        if b == 3:
            print("The data is third person")
def second_person(text):
    word=word2=text
    text = remove_punctuation_parser(text)
    word = remove_punctuation_parser_nolower(word)
    #list of second person pronouns
    second_person_pronouns = ["you", "your", "yours"]
    for i in range(0,len(text)):
        if text[i] in second_person_pronouns:
            print("The '%s' word is a second person pronoun"%text[i])
            return 2
def third_person(text):
    word=word2=text
    text = remove_punctuation_parser(text)
    word = remove_punctuation_parser_nolower(word)
    #list of third person pronouns
    third_person_pronouns = ["he", "him", "his", "she", "her", "hers", "it", "its", "they", "them", "their", "theirs"]
    for i in range(0,len(text)):
        if text[i] in third_person_pronouns:
            print("The '%s' word is a third person pronoun"%text[i])
            return 3
