# load file from shell lines
import sys
documentFile = open(sys.argv[1])
stopwordFile = open(sys.argv[2])

# load stop words into a set
stopwords = stopwordFile.read().strip().split('\n')
stopwordSet = set(stopwords)
stopwordFile.close()

# build dictionary, key-->word, value-->appear times
time = {}
documentWords = documentFile.read().lower().strip().replace('\n', ' ').split(' ')
for documentWord in documentWords :
    if time.has_key(documentWord) :
        time[documentWord] = time[documentWord] + 1
    else :
        time[documentWord] = 1
documentFile.close()

# the document need to be re-opened for future use
documentFile = open(sys.argv[1])

# loop and print
result = []
for line in documentFile :
    tempList = []
    readline = line.strip().lower().split(' ')
    for word in readline :
        if not word in stopwordSet :
            if time[word] > 1 :
                tempList.append(word)
    result.append(tempList)

for output in result :
    print output
