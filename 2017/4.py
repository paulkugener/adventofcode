#!/usr/bin/env python3
from collections import Counter

validPhraseC, validAnagramPhraseC, runChecker = 0, 0, 0

with open("4input.txt", "r") as f:
    for line in f:
        validPhrase = False
        lineList = line.split()
        d = [k for k, v in Counter(lineList).items() if v > 1]
        if not d:
            validPhrase = True
        if validPhrase:
            validPhraseC += 1
            foundAnagram = False
            for i in lineList:
                for j in lineList:
                    if Counter(i) == Counter(j) and i != j:
                        foundAnagram = True
                        runChecker += 1
                        break
                if foundAnagram:
                    break
            if foundAnagram is False:
                validAnagramPhraseC += 1


print("answer1 = {}".format(validPhraseC))
print("anser2 = {}".format(validAnagramPhraseC))
print("checkkk = {}".format(runChecker))
