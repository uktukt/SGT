# write a program that asks for two text inputs s1 and s2 
# you can use better names than s1 and s2
# then checks if all the characters in first string are in second string
# if they are, print All character counts in the second string
# if not, print Not all characters are in the second string
# example
# s1 = "abc"
# s2 = "abracadabra"
# output: a 5, b 2, c 1, d 1, r 2  # so do not print the empty ones
# example two
# s1 = "abc"
# s2 = "def"
# output: Not all characters are in the second string

import string
from collections import OrderedDict

text1 = input("enter 1st text: ")
text2 = input("enter 2nd text: ")
# text1 = "let's try"
# text2 = "let's trryyy"
text3 = text2.replace(" ","")

if len(text1)!=0 and len(text2)!=0:
    for i in text1:

        if not text2.find(i) !=-1:
            print("Not all characters are in the second string")
            break

    if text2.find(i) !=-1:
        d = 1
        while d in range(1,len(text3)):
            d = d+1       
            for c in text3:
                nr = text3.count(c)
                if nr==d:
                    print(c, nr, end=",")
                    break
        for c in text3:
            nr = text3.count(c)
            if nr==1:
                print(c, nr, end=",")
elif len(text1)==0 and len(text2)==0:
    print("Texts not found")
elif len(text1)==0:
    print("1st text not found")
elif len(text2)==0:
    print("2nd text not found")