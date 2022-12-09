import pickle as pkl
data_set = pkl.load(open('.github_materials/autocorrect/txr.dat', 'rb'))
list_set = pkl.load(open('.github_materials/autocorrect/bin.dat', 'rb'))
close_keys = pkl.load(open('.github_materials/autocorrect/close_keys.dat', 'rb'))
commons = pkl.load(open('.github_materials/autocorrect/ofw.dat', 'rb'))
small = pkl.load(open('.github_materials/autocorrect/small.dat', 'rb'))
def isword(word): 
    if word.lower() in list_set.keys(): 
        return True
#make a function to get the edit distance between two words
def edit_distance(word1, word2):
    #make a matrix to store the edit distance
    matrix = [[0 for i in range(len(word1)+1)] for j in range(len(word2)+1)]
    #initialize the matrix
    for i in range(len(word1)+1):
        matrix[0][i] = i
    for i in range(len(word2)+1):
        matrix[i][0] = i
    #calculate the edit distance
    for i in range(1, len(word2)+1):
        for j in range(1, len(word1)+1):
            if word1[j-1] == word2[i-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = min(matrix[i-1][j]+1, matrix[i][j-1]+1, matrix[i-1][j-1]+1)
    return matrix[len(word2)][len(word1)]
def autocorrect(word):
    #this function is used to correct the spelling of a word if it is not in the dictionary
    if word in list_set:
        return [word]
    elif len(word) <=3 and word in small:
        return [word]
    else: 
        #find the word with the smallest edit distance
        #automatically correct the word if the edit distance is less than 
        try:
            if len(word) > 3: 
                print(word)
                start = word[0:3]
                min_distance = 100
                list = [] 
                for i in data_set[word[0]][word[0:2]][start]:
                    distance = edit_distance(word, i)
                    if distance <= min_distance:
                        min_distance = distance
                        min_word = i
                        list.append(min_word)

                final = [] 
                for i in list:
                    try:
                        if  commons[i] ==1:
                            final.append(i)
                    except:
                        pass
                return final[::-1]
            elif len(word) == 3: 
                min_distance = 100
                list = [] 
                for i in small[word[0]]:
                    distance = edit_distance(word, i)
                    if distance <= min_distance:
                        min_distance = distance
                        min_word = i
                        list.append(min_word)
                final = [] 
                try :
                    for i in list:
                        if  commons[i] ==1:
                            print(i)
                            final.append(i)
                    return final[::-1]
                except:
                    pass


        except :
            return 0

"""final = [] 
    clit = close_keys[word[len(word)-1]]
    print(clit)
    print(word)
    for j in clit: 
        wordn=word[0:len(word)-1]
        wordn+=j
        print(wordn)
        if wordn in list:
            final.append(wordn)
    return final
    """