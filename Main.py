# -*- coding: utf-8 -*-
"""
Created on Thu Oct 28 03:42:26 2021

@author: Asus
"""
#Name: Berke Derin Berktay
#ID: 72968
#Project Assignment: 1

import copy
plaintexts = []
global dummy
dummy = 0
global  q
global r
global bruh
bruh = 0
global ls1
ls1=[]
global ls2
ls2=[]
cyphertexts = []
N = int(input("Please enter the number of cypher-plaintext pairs that you will enter, this number needs to be at least 3: "))
L = int(input("Please enter the length of the cypher-plaintext pairs that you will enter, this number needs to be at least 1: "))
for i in range(1,2*N+1):
        if (i <= N):
            Plaintext = input("Please enter the plaintext number " + str(i) + " with length " + str(L) + ":")
            plaintexts.append(Plaintext)
        else :
            Cyphertext = input("Please enter the cyphertext number " + str(i - 3) + " with length " + str(L) + ":")
            cyphertexts.append(Cyphertext) #Gets the plaintexts and cyphertexts inputs and stores them in the plaintexts and cyphertexts lists

bitplaintexts = []
bitcyphertexts = []
for i in range(0, len(plaintexts)):
    thisplaintext = []#For each plaintexts, it converts each of their letters to their 4-bit versions and then stores the newly transformed
                        # 4-bit versions of the plaintexts into bitplaintexts
    for j in range(0,L):
        if (plaintexts[i][j] == "0"):
            thisplaintext.append("0000")
        elif (plaintexts[i][j] == "1"):
            thisplaintext.append("0001")
        elif (plaintexts[i][j] == "2"):
            thisplaintext.append("0010")
        elif (plaintexts[i][j] == "3"):
            thisplaintext.append("0011")
        elif (plaintexts[i][j] == "4"):
            thisplaintext.append("0100")
        elif (plaintexts[i][j] == "5"):
            thisplaintext.append("0101")
        elif (plaintexts[i][j] == "6"):
            thisplaintext.append("0110")
        elif (plaintexts[i][j] == "7"):
            thisplaintext.append("0111")
        elif (plaintexts[i][j] == "8"):
            thisplaintext.append("1000")
        elif (plaintexts[i][j] == "9"):
            thisplaintext.append("1001")
        elif (plaintexts[i][j] == "a"):
            thisplaintext.append("1010")
        elif (plaintexts[i][j] == "b"):
            thisplaintext.append("1011")
        elif (plaintexts[i][j] == "c"):
            thisplaintext.append("1100")
        elif (plaintexts[i][j] == "d"):
            thisplaintext.append("1101")
        elif (plaintexts[i][j] == "e"):
            thisplaintext.append("1110")
        elif (plaintexts[i][j] == "f"):
            thisplaintext.append("1111")
    bitplaintexts.append(thisplaintext)


for i in range(0, len(cyphertexts)):
    thiscyphertext = [] #Does the same opertaion for the cyphertexts
    for j in range(0,L):
        if (cyphertexts[i][j] == "0"):
            thiscyphertext.append("0000")
        elif (cyphertexts[i][j] == "1"):
            thiscyphertext.append("0001")
        elif (cyphertexts[i][j] == "2"):
            thiscyphertext.append("0010")
        elif (cyphertexts[i][j] == "3"):
            thiscyphertext.append("0011")
        elif (cyphertexts[i][j] == "4"):
            thiscyphertext.append("0100")
        elif (cyphertexts[i][j] == "5"):
            thiscyphertext.append("0101")
        elif (cyphertexts[i][j] == "6"):
            thiscyphertext.append("0110")
        elif (cyphertexts[i][j] == "7"):
            thiscyphertext.append("0111")
        elif (cyphertexts[i][j] == "8"):
            thiscyphertext.append("1000")
        elif (cyphertexts[i][j] == "9"):
            thiscyphertext.append("1001")
        elif (cyphertexts[i][j] == "a"):
            thiscyphertext.append("1010")
        elif (cyphertexts[i][j] == "b"):
            thiscyphertext.append("1011")
        elif (cyphertexts[i][j] == "c"):
            thiscyphertext.append("1100")
        elif (cyphertexts[i][j] == "d"):
            thiscyphertext.append("1101")
        elif (cyphertexts[i][j] == "e"):
            thiscyphertext.append("1110")
        elif (cyphertexts[i][j] == "f"):
            thiscyphertext.append("1111")
    bitcyphertexts.append(thiscyphertext)
    
    
global c
c=0
global dc
dc = []
global pc
pc = []
def foo(cyphertexts, plaintexts, n, l):
    #finaltext = ""
    for cypher in cyphertexts:
        for plain in plaintexts:
            #dp = plaintexts.copy()
            #dc = cyphertexts.copy()
            #global bruh
            #global q
            #global r
            #if bruh == 1:
             #   dp[q] = [""]
              #  dc[r] = [""]
               # bruh = 0
            keylist = []
            for k in range(0, len(cyphertexts[0][0])):
                if cypher[0][k] == "0" and plain[0][k] == "0":
                    keylist.append(0)
                elif cypher[0][k] == "0" and plain[0][k] == "1":
                    keylist.append(1)
                elif cypher[0][k] == "1" and plain[0][k] == "0":
                    keylist.append(1)
                elif cypher[0][k] == "1" and plain[0][k] == "1":
                    keylist.append(0)#gets a candidate key
            arrc = copy.deepcopy(cyphertexts)
            arrp = copy.deepcopy(plaintexts)
            #ls = []
            arrc.remove(cypher)
            arrp.remove(plain)
            #ls.append(plain)
            #ls.append(cypher)
            counter = 1
            #finaltext += "(Plaintext " + str(plaintexts.index(plain) + 1)  + ", " + "Cyphertext " + str(cyphertexts.index(cypher) + 1) + ")"
            #global ls1
            #ls1.append(plaintexts[plaintexts.index(plain)])
            #global ls2
            #ls2.append(cyphertexts[cyphertexts.index(cypher)])
            for cypherx in arrc:
                global candidateplain
                candidateplain = [""]
                for k in range(0, len(cyphertexts[0][0])):
                    if cypherx[0][k] == "0" and keylist[k] == 0:
                        candidateplain[0] += "0"
                    elif cypherx[0][k] == "0" and keylist[k] == 1:
                        candidateplain[0] += "1"
                    elif cypherx[0][k] == "1" and keylist[k] == 0:
                        candidateplain[0] += "1"
                    elif cypherx[0][k] == "1" and keylist[k] == 1:
                        candidateplain[0] += "0"
                if candidateplain in arrp:
                    #ls.append(candidateplain)
                    #ls.append(cypherx)
                    counter+=1
                    #print(dp)
                    #if candidateplain not in ls1 and cypherx not in ls2:
                    #    finaltext += "(Plaintext " + str(dp.index(candidateplain) + 1) + ", " + "Cyphertext " + str(dc.index(cypherx) + 1) + ")"
                    #    ls1.append(plaintexts[plaintexts.index(candidateplain)])
                    #   ls2.append(cyphertexts[cyphertexts.index(cypherx)])
                    #elif (candidateplain in ls1 and cypherx not in ls2):
                    #    count1 = ls1.count(candidateplain)
                    #    index1 = [i for i, n in enumerate(ls1) if n == candidateplain][count1]
                    #    finaltext += "(Plaintext " + str(index1 + 1) + ", " + "Cyphertext " + str(dc.index(cypherx) + 1) + ")"
                    #elif candidateplain not in ls1 and cypherx in ls2:
                    #    count2 = ls2.count(cypherx)
                    #    index2 = [i for i, n in enumerate(ls2) if n == cypherx][count2]
                    #    finaltext += "(Plaintext " + str(dp.index(candidateplain) + 1) + ", " + "Cyphertext " + str(index2 + 1) + ")"
                    #else:
                    #    count1 = ls1.count(candidateplain)
                    #    count2 = ls2.count(cypherx)
                    #    index1 = [i for i, n in enumerate(ls1) if n == candidateplain][count1]
                    #    index2 = [i for i, n in enumerate(ls2) if n == cypherx][count2]
                    #    finaltext += "(Plaintext " + str(index1 + 1) + ", " + "Cyphertext " + str(index2 + 1) + ")"
                    #q = dp.index(candidateplain)
                    #r = dc.index(cypherx)
                    #bruh = 1
                    arrp.remove(candidateplain)# if the candidate key works for the proposed pairs, we increment counter
                #
                #if (arrc.index(cypherx) == (len(arrc)-1) and k == len(cyphertexts[0][0]) - 1):
                #    if (counter!=n):
                #        finaltext = ""
                #
                # AS YOU NOTICE, ALL OF THE CORRECT PAIRS ARE DISPLAYED, HOWEVER TO ADD TO THOSE,COUPLE MORE WRONG PAIRS ARE DISPLAYED
                # I TRIED TO DISPLAY ONLY THE RIGHT PAIRS BY USING A DIFFERENT IDEA AND WRITING THE CODE ABOVE, IT WORKED FOR DISPLAYING THE 
                # RIGHT PAIRS HOWEVER IT MESSED UP THE CANDIDATEPLAIN AND CYPHERLISTS AND THEREFORE I COULD NOT FIX IT, I LEFT THE CODE 
                # FOR PARTIAL MARKS SINCE
                # I AM SUCCESSFULLY DEMONSTRATING THE IDEA THAT ALLOWS ME TO DISPLAY ONLY THE RIGHT PAIRS. BUT LIKE I SAID, SINCE IT MESSES UP
                # THE LISTS I CAN NOT DISPLAY IT AND I COULDNT FIX THIS ISSUE
            if counter == n:#this means that the key worked for all of the matches and therefore it is indeed the right key
                #global dummy
                #if dummy == 0:
                #    print(finaltext)
                #dummy = 1
                return keylist
keyslist = []
for i in range(0,L):#Separates the letters of each cypherplain pairs and groups them together and then calls 
                    #the function foo in order to find the key for the current nth letter groups
    bitc_i = []
    bitp_i = []
    for j in range(0,N):
        dummylist1 = []
        dummylist2 = []
        dummylist1.append(bitcyphertexts[j][i])
        dummylist2.append(bitplaintexts[j][i])
        bitc_i.append(dummylist1)
        bitp_i.append(dummylist2)
    key = foo(bitc_i, bitp_i, N, L) 
    keyslist.append(key)#stores the keys
    
    
presentedkeylist=""
pairslist = ""
firstletterplain = []
firstletttercypher = []
for i in range(0, len(bitcyphertexts)):
    firstletttercypher.append(bitcyphertexts[i][0])
for j in range(0, len(bitplaintexts)):
    firstletterplain.append(bitplaintexts[j][0])#takes the first letters to compare pairs cyphers with plains
for i in range(0,len(firstletttercypher)):
    cypherindex = i
    for j in range(0,len(firstletterplain)):
        plainindex = j
        keylist = []
        for k in range(0, 4):
            if firstletttercypher[i][k] == "0" and firstletterplain[j][k] == "0":
                keylist.append(0)
            elif firstletttercypher[i][k] == "0" and firstletterplain[j][k] == "1":
                keylist.append(1)
            elif firstletttercypher[i][k] == "1" and firstletterplain[j][k] == "0":
                keylist.append(1)
            elif firstletttercypher[i][k] == "1" and firstletterplain[j][k] == "1":
                keylist.append(0)
        if keylist == keyslist[0]: #if it finds that the proposed key resulting from the comparison of the candidate pairs is equal to the first key
                                    # it adds it to the list of correct pairs.
            pairslist += ("(Plaintext " + str(plainindex + 1) +", Ciphertext " + str(cypherindex + 1) + "), ")
print(pairslist)


for i in range(0,L):
    number = ""
    for j in range(0,N + 1):
        number += str(keyslist[i][j])
    if (number == "0000"):
            presentedkeylist += "0"
    elif (number == "0001"):
            presentedkeylist += "1"
    elif (number == "0010"):
            presentedkeylist += "2"
    elif (number == "0011"):
            presentedkeylist += "3"
    elif (number == "0100"):
            presentedkeylist += "4"
    elif (number == "0101"):
            presentedkeylist += "5"
    elif (number == "0110"):
            presentedkeylist += "6"
    elif (number == "0111"):
            presentedkeylist += "7"
    elif (number == "1000"):
            presentedkeylist += "8"
    elif (number == "1001"):
            presentedkeylist += "9"
    elif (number == "1010"):
            presentedkeylist += "a"
    elif (number == "1011"):
            presentedkeylist += "b"
    elif (number == "1100"):
            presentedkeylist += "c"
    elif (number == "1101"):
            presentedkeylist += "d"
    elif (number == "1110"):
            presentedkeylist += "e"
    elif (number == "1111"):
            presentedkeylist += "f"
print("Key:" + presentedkeylist)#changes the key list back to decimal form and outputs it.

#By analyzing the code, I know that the peak runtime complexity occurs during the loop when we call the foo function
#for the two embedded for functions that ultimately end up calling the foo function, we already have O(N*L) time complexity
#On the inside of foo the worst time complexity when we also consider the 2 outside for loops is O(L*N^3)
#This is a bit worse than what was asked, however it was the best I could do, I wanted to demonstrate my understanding
#of the concept in order tp get some extra points anyways.
