'''
Assigment 2: Text analyzer
finding the fingerprint of different languages
29.4.2014 
@author: etodorov
'''
#raw data about the languages, 3 digit accuracy in %
# Distribution of word length [0letters, 1letter, 2letters, 3letters,...]
wordDistr_english = [0, 1.377, 17.63, 21.212, 9.641, 10.468, 7.162, 6.887, 9.366, 5.509, 2.754, 2.754, 4.683, 0, 0, 0.55, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# Frequency of use of letters [a,b,c,d,...]
fqLetters_english = [7.338, 1.67, 3.694, 3.744, 14.17, 2.074, 1.72, 4.605, 7.995, 0.0, 0.404, 3.542, 2.53, 7.641, 7.489, 2.226, 0.05, 6.325, 6.831, 9.311, 1.923, 1.923, 0.657, 0.607, 1.417, 0.101]
wordDistr_french = [0, 1.166, 25.947, 19.241, 10.204, 8.163, 9.62, 4.373, 7.288, 4.081, 3.206, 2.915, 2.04, 0.874, 0, 0.874, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fqLetters_french = [7.584, 1.516, 3.306, 5.445, 14.702, 0.622, 1.555, 0.933, 7.156, 0.233, 0.077, 6.651, 2.489, 8.012, 5.989, 3.422, 1.478, 6.067, 7.934, 6.106, 6.378, 1.4, 0.077, 0.622, 0.233, 0.0]
wordDistr_german = [0, 1.857, 5.263, 30.65, 12.693, 10.216, 6.191, 6.811, 7.43, 2.167, 6.191, 3.405, 0.619, 1.857, 2.167, 0.928, 0, 0.309, 0.309, 0.619, 0, 0.309, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fqLetters_german = [4.966, 1.399, 2.663, 5.101, 16.839, 1.625, 2.663, 4.966, 9.164, 0.135, 1.489, 3.792, 2.573, 8.668, 3.069, 0.948, 0.18, 8.216, 5.372, 6.997, 4.514, 1.534, 1.851, 0.045, 0.451, 0.767]
wordDistr_dutch = [0, 0, 15.789, 26.578, 10.789, 6.578, 9.736, 9.21, 5.0, 5.0, 3.421, 3.157, 0.789, 1.315, 0.789, 0.789, 0.263, 0, 0, 0.789, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
fqLetters_dutch = [7.139, 1.819, 1.773, 5.911, 19.054, 0.5, 2.319, 4.047, 6.321, 1.591, 1.5, 4.638, 2.773, 8.503, 6.775, 0.864, 0.0, 6.957, 4.138, 7.094, 1.227, 2.546, 1.318, 0.136, 0.136, 0.909]


#get the name of the tested file
fileName = raw_input("Give file name (with the extenision)")
#clear the name of the tested file
fileName = fileName.lstrip().rstrip()
#open the file
fTested = open("D:/Evgeni/My Studies/Aerospace/Python/TextAnalyzer/"+fileName, "r")
#assure the file
if(fTested): print "Found "+fileName+", reading and analyzing it."
else: 
    print "Give a valid file name"    
    fTested.close
#read file
txt=fTested.read()
fTested.close()
#prepare the text
#lower case, clean commas, dots  and new line
txt = txt.lower()
txt = txt.replace(","," ").replace("."," ").replace("!", " ").replace("?", " ").replace("\n", " ")

#get the number of occurances of each letter
totLetters = 0
fqLetters = 200*[0]
#go over each letter in the text
letters = txt.replace(" ","")
for letter in letters:
    if letter.isalpha():
        fqLetters[(ord(letter)-97)]+=1
        totLetters +=1
#clear everything but latin alphabet
fqLetters = fqLetters[:26]
#get the percentage and prepare a string
txt_fqLetters = "Frequency of letters \n"
for l in range(26): 
    fqLetters[l]=float(fqLetters[l])/totLetters
    txt_fqLetters+= chr(65+l)+": \t"+str(fqLetters[l]*100)+"% \n"
#print the result
print txt_fqLetters

#get the word length distribution
#split by whitespace
words = txt.split()
#count the words and get their length 
numWords=0
wordDistr=50*[0]
for word in words:
    #check if word
    if(word.isalpha()):
        #one more words
        numWords+=1
        #one more word with this length
        wordDistr[len(word)]+=1
#get percentages and prepare string
txt_wordDistr="Word distribution \n"
for k in range(1,len(wordDistr)):
    if(wordDistr[k]!=0):
        wordDistr[k]=float(wordDistr[k])/numWords
        txt_wordDistr += str(wordDistr[k]*100)+"% \t of the words are length \t"+str(k)+"\t characters \n"
#print the result
print txt_wordDistr

#compare the data about the text with the raw data about the languages
#add a point for every close enough comparison
eng=0
de=0
fr=0
nl=0
#points for word distribution
for i in range(len(wordDistr)):
    if((abs(wordDistr[i]*100-wordDistr_english[i])/(wordDistr_english[i]+0.0001))<0.1):
        eng +=1
    if((abs(wordDistr[i]*100-wordDistr_french[i])/(wordDistr_french[i]+0.0001))<0.1):
        fr +=1
    if((abs(wordDistr[i]*100-wordDistr_german[i])/(wordDistr_german[i]+.0001))<0.1):
        de +=1
    if((abs(wordDistr[i]*100-wordDistr_dutch[i])/(wordDistr_dutch[i]+.0001))<0.1):
        nl +=1     
#points for letter frequency
for j in range(len(fqLetters)):
    if((abs(fqLetters[j]*100-fqLetters_english[j])/(fqLetters_english[j]+0.0001))<0.5):
        eng +=1
    if((abs(fqLetters[j]*100-fqLetters_french[j])/(fqLetters_french[j]+0.0001))<0.5):
        fr +=1
    if((abs(fqLetters[j]*100-fqLetters_german[j])/(fqLetters_german[j]+.0001))<0.5):
        de +=1
    if((abs(fqLetters[j]*100-fqLetters_dutch[j])/(fqLetters_dutch[j]+.0001))<0.5):
        nl +=1

#determine the language according to score
if(eng>fr): x = eng
elif(eng<fr): x = fr
else: x = 1000
if(x<de):x=de
if(x<nl):x=nl
#print results
result = "This text is probably in "
if(x==eng):
    result += "English"
elif(x==fr):
    result += "French"
elif(x==de):
    result += "German"
elif(x==nl):
    result += "Dutch"
else:
    result = "Can't be determined accurately"

print result


