'''
Assigment 2: Text analyzer
finding the fingerprint of different languages
29.4.2014 
@author: etodorov
'''

#get the name of the tested file
fileName = "english.txt"#raw_input("Give file name (with the extenision)")
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
wordDistr=20*[0]
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

    wordDistr[k]=float(wordDistr[k])/numWords
    txt_wordDistr += str(wordDistr[k]*100)+"% \t of the words are length \t"+str(k)+"\t characters \n"
#print the result
print txt_wordDistr


fTested.close()
