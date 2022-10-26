# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:59:59 2022
@author: segal
"""
import csv 
import copy
# global counter
counter = 0
# after importing the csv files the create a func
# to do the insertion sort thru the files
# break a part lists: like his example ? ! hm. just stats  * fix to only stats

# so do 9 of these:
# list 1:
file = open("pokemonRandomLarge.csv", "r")
text = file.readlines()
# may remove pokemonRandomLarge = [] # new empty list
text.pop(0)
pokemonRandomLarge_insert = [] # 1st copy
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonRandomLarge_insert.append(text[i][1])
    
pokemonRandomLarge_merge= copy.deepcopy(pokemonRandomLarge_insert) 
pokemonRandomLarge_quick= copy.deepcopy(pokemonRandomLarge_insert) 
# list 2 and onward:    
file = open("pokemonRandomMedium.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonRandomMedium_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonRandomMedium_insert.append(text[i][1])
    
pokemonRandomMedium_merge= copy.deepcopy(pokemonRandomMedium_insert) 
pokemonRandomMedium_quick= copy.deepcopy(pokemonRandomMedium_insert) 

file = open("pokemonRandomSmall.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonRandomSmall_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonRandomSmall_insert.append(text[i][1])
    
pokemonRandomSmall_merge= copy.deepcopy(pokemonRandomSmall_insert) 
pokemonRandomSmall_quick= copy.deepcopy(pokemonRandomSmall_insert) 

file = open("pokemonSortedLarge.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonSortedLarge_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonSortedLarge_insert.append(text[i][1])
    
pokemonSortedLarge_merge= copy.deepcopy(pokemonSortedLarge_insert) 
pokemonSortedLarge_quick= copy.deepcopy(pokemonSortedLarge_insert) 

#SortedLarge
file = open("pokemonSortedMedium.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonSortedMedium_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonSortedMedium_insert.append(text[i][1])
    
pokemonSortedMedium_merge= copy.deepcopy(pokemonSortedMedium_insert) 
pokemonSortedMedium_quick= copy.deepcopy(pokemonSortedMedium_insert) 
#SortedSmall
file = open("pokemonSortedSmall.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonSortedSmall_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonSortedSmall_insert.append(text[i][1])
    
pokemonSortedSmall_merge= copy.deepcopy(pokemonSortedSmall_insert) 
pokemonSortedSmall_quick= copy.deepcopy(pokemonSortedSmall_insert) 

file = open("pokemonReverseSortedLarge.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonReverseSortedLarge_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonReverseSortedLarge_insert.append(text[i][1])
    
pokemonReverseSortedLarge_merge= copy.deepcopy(pokemonReverseSortedLarge_insert) 
pokemonReverseSortedLarge_quick= copy.deepcopy(pokemonReverseSortedLarge_insert) 

file = open("pokemonReverseSortedMedium.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonReverseSortedMedium_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonReverseSortedMedium_insert.append(text[i][1])
    
pokemonReverseSortedMedium_merge= copy.deepcopy(pokemonReverseSortedMedium_insert) 
pokemonReverseSortedMedium_quick= copy.deepcopy(pokemonReverseSortedMedium_insert) 

file = open("pokemonReverseSortedSmall.csv", "r")
text = file.readlines()

text.pop(0)
statsList = []
pokemonReverseSortedSmall_insert = [] # new empty list
for i in range(len(text)):
	text[i] = text[i].rstrip("\n")
	text[i] = text[i].split(",")
	text[i][1] = int(text[i][1])
	pokemonReverseSortedSmall_insert.append(text[i][1])
    
pokemonReverseSortedSmall_merge= copy.deepcopy(pokemonReverseSortedSmall_insert) 
pokemonReverseSortedSmall_quick= copy.deepcopy(pokemonReverseSortedSmall_insert) 
# insertion sort
# index through 
# 1st fileNames into an array 
# leave it as 1-D
# maybe delete this and use !! his way:

#the array or (arr) I want to put into this sort is called fileName
def insertionSort(listName): # fileName 
    global counter
    # Run file_to_arr on filename *
    # sortDict= file_to_arr(filename) *
    # traverse through 1 to len(fileName)
    #for i in sortDict.keys() ?
    for i in range(1, len(listName)): # x had a mistake 
        
        key = listName[i]
        # move elements of fileName[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
       
        
        while j >= 0 and key < listName[j]: # may have messed up with a dictionary. 
        
            listName[j + 1] = listName[j]
            counter += 1
            j -= 1
        counter += 1
        listName[j + 1] = key
   
    # A is input list or X, p-1st index?, q-the middle, r-end
def merge(X, p, q, r):
    global counter
    # compare - later
    n1 = q - p + 1
    n2 = r - q # to get len of right sub-array  
    
    Lefty = [0]*n1
    Righty = [0]*n2
    
    for i in range(0, n1):
        Lefty[i] = X[p + i]
    for j in range(0, n2):
        Righty[j] = X[q + j + 1]
    # reset i,j, and k, or change variables
    i = 0
    j = 0
    k = p
    counter = 0
    while i < n1 and j < n2: # check edge cases !!
        counter += 1
        if Lefty[i] < Righty[j]:
            X[k] = Lefty[i]
            i += 1
        
        else:
            X[k] = Righty[j]
            j += 1
        k += 1
    # may remove - X  ? instead .append and maybe change the while loop to his for-loop
    
    while i < n1:
        X[k] = Lefty[i]
        i += 1
        k += 1
        
    while j < n2:
        X[k] = Righty[j] # fix it. !
        j += 1
        k += 1
# call the merge sort function
def mergeS (X, p, r):
    if p < r:      
        q = 0
        q = p + ( r - p ) // 2 # maybe try. it might overflow ? why undefined   q ? do a ceiling ? 
        
        mergeS(X, p, q)      
        mergeS(X, q + 1, r)
        merge(X, p, q, r)
       
def QuickS(X, p, r):
    # countz - for comparing
    
    if p < r:
        q  = partition(X, p, r) 
        
        QuickS(X, p, q-1)
        QuickS(X, q+1, r)
        
def partition(X, p, r):
    global counter 
    pivot =  X[r]
    
    i = p -1
    
    for j in range(p, r):
        counter += 1
        if X[j] <= pivot:
            i = i + 1
            
            X[i], X[j] = X[j], X[i] 
            
        X[i + 1], X[r] = X[r], X[i+1] # swap 
        
        return i+1
# this needs to be done 27 times
# section A for insertion
# insertion 1st:
counter = 0
insertionSort(pokemonRandomLarge_insert)
print(pokemonRandomLarge_insert, "\n\nThis compares insertion for pokemon in a Random large list for insertion")
print("\ncompares counter: "+str(counter))

# 2nd the pokemonRandomMedium_insert
counter = 0
insertionSort(pokemonRandomMedium_insert)
print(pokemonRandomMedium_insert, "\n\nThis compares insertion for pokemon in a Random Medium list for insertion")
print("\ncompares counter: "+str(counter))

# 3rd the pokemonRandomSmall_insert
# pokemonRandomSmall_insert
counter = 0
insertionSort(pokemonRandomSmall_insert)
print(pokemonRandomSmall_insert, "\n\nThis compares insertion for pokemon in a Random Small list for insertion")
print("\ncompares counter: "+str(counter))

# 4: pokemonSortedLarge_insert

counter = 0
insertionSort(pokemonSortedLarge_insert)
print(pokemonSortedLarge_insert, "\n\nThis compares insertion for pokemon in a Sorted Large list for insertion")
print("\ncompares counter: "+str(counter))
# 5:
#pokemonSortedMedium_insert
counter = 0
insertionSort(pokemonSortedMedium_insert)
print(pokemonSortedMedium_insert, "\n\nThis compares insertion for pokemon in a Sorted Medium list for insertion")
print("\ncompares counter: "+str(counter))

# 6:
#pokemonSortedSmall_insert
counter = 0
insertionSort(pokemonSortedSmall_insert)
print(pokemonSortedSmall_insert, "\n\nThis compares insertion for pokemon in a Sorted Small list for insertion")
print("\ncompares counter: "+str(counter))
# 7:
#pokemonReverseSortedLarge_insert
counter = 0
insertionSort(pokemonReverseSortedLarge_insert)
print(pokemonReverseSortedLarge_insert, "\n\nThis compares insertion for pokemon in a Reverse Sorted Large list for insertion")
print("\ncompares counter: "+str(counter))
# 8:
#pokemonReverseSortedMedium_insert
counter = 0
insertionSort(pokemonReverseSortedMedium_insert)
print(pokemonReverseSortedMedium_insert, "\n\nThis compares insertion for pokemon in a Reverse Sorted Medium list for insertion")
print("\ncompares counter: "+str(counter))
# 9:
counter = 0
insertionSort(pokemonReverseSortedSmall_insert)
print(pokemonReverseSortedSmall_insert, "\n\nThis compares insertion for pokemon in a Reverse Sorted Small list for insertion")
print("\ncompares counter: "+str(counter))    

# section B for Quick Sort
# Quick 1st: large random
counter = 0
QuickS(pokemonRandomLarge_quick, 0, len(pokemonRandomLarge_quick)-1)
print(pokemonRandomLarge_quick, "\n\nThis compares Quick for pokemon in a Random large list for Quick")
print("\ncompares counter: "+str(counter))  

# 2: medium random
counter = 0
QuickS(pokemonRandomMedium_quick, 0, len(pokemonRandomMedium_quick)-1)
print(pokemonRandomMedium_quick, "\n\nThis compares Quick for pokemon in a Random Medium list for Quick")
print("\ncompares counter: "+str(counter))  
# 3: small random
counter = 0
QuickS(pokemonRandomSmall_quick, 0, len(pokemonRandomSmall_quick)-1)
print(pokemonRandomSmall_quick, "\n\nThis compares Quick for pokemon in a Random Small list for Quick")
print("\ncompares counter: "+str(counter))  
# 4. sortted Large
counter = 0
QuickS(pokemonSortedLarge_quick, 0, len(pokemonSortedLarge_quick)-1)
print(pokemonSortedLarge_quick, "\n\nThis compares Quick for pokemon in a Sorted Large list for Quick")
print("\ncompares counter: "+str(counter))  
# 5. Sorted Medium
counter = 0
QuickS(pokemonSortedMedium_quick, 0, len(pokemonSortedMedium_quick)-1)
print(pokemonSortedMedium_quick, "\n\nThis compares Quick for pokemon in a Sorted Medium list for Quick")
print("\ncompares counter: "+str(counter))  
# 6. sorted small
counter = 0
QuickS(pokemonSortedSmall_quick, 0, len(pokemonSortedSmall_quick)-1)
print(pokemonSortedSmall_quick, "\n\nThis compares Quick for pokemon in a Sorted Small list for Quick")
print("\ncompares counter: "+str(counter))  
# 7. reversed Large
counter = 0
QuickS(pokemonReverseSortedLarge_quick, 0, len(pokemonReverseSortedLarge_quick)-1)
print(pokemonReverseSortedLarge_quick, "\n\nThis compares Quick for pokemon in a revere Sorted large list for Quick")
print("\ncompares counter: "+str(counter)) 
# 8
counter = 0
QuickS(pokemonReverseSortedMedium_quick, 0, len(pokemonReverseSortedMedium_quick)-1)
print(pokemonReverseSortedMedium_quick, "\n\nThis compares Quick for pokemon in a revere Sorted medium list for Quick")
print("\ncompares counter: "+str(counter)) 
# 9
counter = 0
QuickS(pokemonReverseSortedSmall_quick, 0, len(pokemonReverseSortedSmall_quick)-1)
print(pokemonReverseSortedSmall_quick, "\n\nThis compares Quick for pokemon in a revere Sorted small list for Quick")
print("\ncompares counter: "+str(counter)) 
# section C for Merge
# Merge 1st: 
# 1. random large
counter = 0
mergeS(pokemonRandomLarge_merge, 0, len(pokemonRandomLarge_merge)-1)
print(pokemonRandomLarge_merge, "\n\nThis compares merge for pokemon in a Random large list for merge")
print("\ncompares counter: "+str(counter))    
# 2. random med.
counter = 0
mergeS(pokemonRandomMedium_merge, 0, len(pokemonRandomMedium_merge)-1)
print(pokemonRandomMedium_merge, "\n\nThis compares merge for pokemon in a Random medium list for merge")
print("\ncompares counter: "+str(counter))  
# 3. random small
counter = 0
mergeS(pokemonRandomSmall_merge, 0, len(pokemonRandomSmall_merge)-1)
print(pokemonRandomSmall_merge, "\n\nThis compares merge for pokemon in a Random small list for merge")
print("\ncompares counter: "+str(counter))  
# 4. sorted large
counter = 0
mergeS(pokemonSortedLarge_merge, 0, len(pokemonSortedLarge_merge)-1)
print(pokemonSortedLarge_merge, "\n\nThis compares merge for pokemon in a sorted large list for merge")
print("\ncompares counter: "+str(counter))  
# 5. sorted Med.
counter = 0
mergeS(pokemonSortedMedium_merge, 0, len(pokemonSortedMedium_merge)-1)
print(pokemonSortedMedium_merge, "\n\nThis compares merge for pokemon in a sorted medium list for merge")
print("\ncompares counter: "+str(counter))  
# 6. sorted small
counter = 0
mergeS(pokemonSortedSmall_merge, 0, len(pokemonSortedSmall_merge)-1)
print(pokemonSortedSmall_merge, "\n\nThis compares merge for pokemon in a sorted small list for merge")
print("\ncompares counter: "+str(counter))  
# 7. reversed sorted Large
counter = 0
mergeS(pokemonReverseSortedLarge_merge, 0, len(pokemonReverseSortedLarge_merge)-1)
print(pokemonReverseSortedLarge_merge, "\n\nThis compares merge for pokemon in a reverse sorted large list for merge")
print("\ncompares counter: "+str(counter))  
# 8. reverse sorted small
counter = 0
mergeS(pokemonReverseSortedMedium_merge, 0, len(pokemonReverseSortedMedium_merge)-1)
print(pokemonReverseSortedMedium_merge, "\n\nThis compares merge for pokemon in a reverse sorted medium list for merge")
print("\ncompares counter: "+str(counter))  
# 9. for reverse sorted small
counter = 0
mergeS(pokemonReverseSortedSmall_merge, 0, len(pokemonReverseSortedSmall_merge)-1)
print(pokemonReverseSortedSmall_merge, "\n\nThis compares merge for pokemon in a reverse sorted small list for merge")
print("\ncompares counter: "+str(counter))  