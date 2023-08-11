import numpy as np
import itertools

#read from file
fileread = open("Lincoln.txt", "r")
stopwords = [ 'stop', 'the', 'to', 'and', 'a', 'in', 'it', 'is', 'I', 'that', 'had', 'on', 'for', 'were', 'was', 'an' ]

wordDic = {}

for line in fileread:    #looks over entire file

    line = line.lower()
    line = line.replace(',' , '')
    line = line.replace('.' , '')

    for word in line.split():    #gets word by word
        
		#place in dictionary
        if word in wordDic:
            temp = wordDic[word]
            temp = temp + 1
            wordDic[word] = temp
        
        if not word in wordDic:
            #wordDic.update({word : 1})
            wordDic[word] = 1

#sort by value
keys = list(wordDic.keys())
values = list(wordDic.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

#shows all sorted items in dictionary
print(sorted_dict)

#top 10
print("\n---top 10 words ---")
listDict = list(sorted_dict.items())    
length = len(sorted_dict) - 1
limit = length
while (length-10) != limit:
    print(listDict[limit])
    limit = limit - 1

#top 10 excluding stop words
print("\n---top 10 words excluding stop words---")
index = length
limit = 0
#value = max(sorted_dict)
#tempword = max(wordDic)
#index?
dic_with_no_stopwords = wordDic

#remove stop words
for a in stopwords:
    if a in dic_with_no_stopwords:
        del dic_with_no_stopwords[a]

#sort by value again
keys = list(dic_with_no_stopwords.keys())
values = list(dic_with_no_stopwords.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}

#display results
listDict = list(sorted_dict.items())
length = len(sorted_dict) - 1
limit = length
while (length-10) != limit:
    print(listDict[limit])
    limit = limit - 1







#print(list(sorted_dict.items()))

