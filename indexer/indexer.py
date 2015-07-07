from string import *

# Program to index sentences

# Author: Daniel Kasprowicz

# Date: 2/12/2011

stopWords = [ "a", "i", "it", "am", "at", "on", "in", "to", "too", "very", \
              "of", "from", "here", "even", "the", "but", "and", "is", "my", \
              "them", "then", "this", "that", "than", "though", "so", "are" ]

punctuation = [".",",", ":", ";", "!", "?", "&", "'"]

endings = ["s", "es", "ed", "er", "ly", "ing"]

def remove(txt):
    noPunc=""
    a = 0

    for i in range(len(txt)):
        for j in range(len(txt[i])):
            for k in punctuation:
               if txt[i][j] != k:
                    a+=1

            if a == 8:
                    

                noPunc += txt[i][j]

            a=0
            
        txt[i] = noPunc.lower()
        noPunc = ""
    return txt


text =[]
i = 0
print "Indexer: type in lines, finish with a . at start of line only: "

while i!=1:
    textTemp = raw_input()

    if textTemp == ".":
        i = 1
    else:
        text+=[textTemp]

remove(text)


temp = ""
noSpace =[]
for i in range(len(text)):
    text[i] = text[i].split()
b = 0
temp=[]
for i in range(len(text)):
    for j in text[i]:
        for a in stopWords:
            if j != a:
                
               b+=1

        if b == 27:
            temp+=[j]
        b =0
    text[i]=temp
    temp =[]

def stem(txt):
    for i in range(len(txt)):
        for j in range(len(txt[i])):
            if txt[i][j][len(txt[i][j])-3:len(txt[i][j])] == "ing":
                txt[i][j] = txt[i][j][:len(txt[i][j])-3]
                if txt[i][j][len(txt[i][j])-3:len(txt[i][j])] == "ing" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ly" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "er" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ed" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "es" or txt[i][j][len(txt[i][j])-1:len(txt[i][j])] == "s":
                    stem(txt)
            elif txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ly" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "er" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ed" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "es":
                txt[i][j] = txt[i][j][:len(txt[i][j])-2]
                if txt[i][j][len(txt[i][j])-3:len(txt[i][j])] == "ing" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ly" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "er" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ed" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "es" or txt[i][j][len(txt[i][j])-1:len(txt[i][j])] == "s":
                    stem(txt)
            elif txt[i][j][len(txt[i][j])-1:len(txt[i][j])] == "s":
                txt[i][j] = txt[i][j][:len(txt[i][j])-1]
                if txt[i][j][len(txt[i][j])-3:len(txt[i][j])] == "ing" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ly" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "er" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "ed" or txt[i][j][len(txt[i][j])-2:len(txt[i][j])] == "es" or txt[i][j][len(txt[i][j])-1:len(txt[i][j])] == "s":
                    stem(txt)

    return txt

stem(text)

#print text


index =[]
a=0

for i in range(len(text)):
    for j in range(len(text[i])):
        if i==0 and j==0:
            index += [[text[i][j],[i+1]]]
        else:
            
            for k in range(len(index)):
                if text[i][j] == index[k][0]:

                    print i+1,
                    print index[k][1]
                    
                    if i+1 not in index[k][1]:
                        index[k][1]+=[i+1]
                    a=0
                    break                               #terminate the 'for k' loop when a match is found
                if text[i][j] != index[k][0]:           #keyword not in index
                    a+=1
                if a == len(index):                    #if a is equal to length, ie no matches in the index,
                    index += [[text[i][j],[i+1]]]      #add a word to index
                                                        
                    a=0

print "The index is: "

for i in range(len(index)):
        
    
    print index[i][0],
    for j in range(len(index[i][1])):
        print index[i][1][j],
    print
    #pass


















    
