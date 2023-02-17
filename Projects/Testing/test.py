from turtle import pen
from numpy import array

#====================Basices code to cal the avareg=================================
def AvaregCal():
    resutl =int(input("Enter Avarege: "))
    yeare =int(input("Enter yeare: "))
    local_1 =str(input("Enter city: "))
    dgree = int(input("Enter dgree: "))
    if resutl >= 90 and yeare >= 3 and local_1 in 'Gaza':
        print("Accept")
    else:
        print("Rejected")
        if dgree in range(80,90):
            dgree +=5
            print(dgree)
        else:
            print("dgree is not between 90 or 80 !!!")
# AvaregCal()

#===================Make list of nuumber a list of string==================================
# Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.
number = [1,2,3,4,5,6,7,8,9,0]
def create_phone_number(n):
    f = "".join(map(str, n[0:3]) )
    s = "".join(map(str, n[3:6]) )
    t = "".join(map(str, n[6:10]) )
    return "("+f+") "+ s +"-"+t 
# print(create_phone_number(number))

#==================array matrix====================
letters = [chr(x) for x in range(ord('a'),ord('z')+1)]
def grid(N):
    for i in range(N):
        for j in range(i, N+i):
            print(letters[j], end=' ')
            if j == N+i-1:
                print('')   #to move to next line
            elif N == '':
                return print('None')

#================if true print yes if false print no =====================================
def bool_to_word(boolean):
    if boolean == True:
        return print('Yes')
    else:
        return print('No')
# bool_to_word(True)

#======================Smash Sentece==================
word=['hello', 'world', 'this', 'is', 'great']
def smash(words):
  return print("'"+" ".join(words) + "'")
# smash(word)

# a=int(input("Number of elements in the array:-"))
# n=list(map(int, input("elements of array:-").split()))
# print(n)

#======translat from DNA TO AND=======================
dna = "GACCGCCGCC"
def dna_to_rna(dna) :
    l = list(dna)  
    for i in range(len(dna)):
        if(l[i]=='G'):
            l[i]='G'
        elif(l[i]=='C'):
            l[i]='C'
        elif (l[i] == 'T'):
            l[i] = 'U'
        elif (l[i] == 'A'):
            l[i] = 'A'
        else:
            print('Invalid Input')                      
    for char in l:
        print(char,end="")
# dna_to_rna(dna)

#==================Sum Array========================
def sum_array(arr):
    if arr == None or len(arr) < 3:
        return 0
    return sum(arr)-max(arr)-min(arr)

# print(sum_array([6,2,1,8,10]))

#==================String to Array==================
def string_to_array(s):
    arr = [ x.strip() for x in string.strip('[]').split(',') ]
    print (arr)
['abcd', 'abc', 'a', 'b', 'abc']
string = "[ab cd, a[b]c, a, b, abc ,13 ,GW]"

# string_to_array(string)

#=============Covncer String to Array as letter or word==========
s = "Hallow My Name is Ali"
s2 = "I love arrays they are my favorite" 
def string_to_array(s,s2):
    print(list(s))
    print(s2.split())
# string_to_array(s,s2)

#==============Sum the number as spilt number as 885 is 8 + 8 +5 ============
def sum_digits(number):
    return sum(int(d) for d in str(abs(number)))
n = 855
# print(sum_digits(n))

# ================Growth of a Population how to cal the population of the pepeole from the currnet number of them======================
def nb_year(p0, percent, aug, p):
 #1000 + 1000 * 0.02 + 50
    no_of_year = 1
    total_population_year = (p0 + int(p0 * (percent/100)) + aug)
    while p > total_population_year:
        no_of_year += 1
        p0 = total_population_year
        total_population_year = (p0 + int(p0 * (percent/100)) + aug)
    return no_of_year
# print(nb_year(1500000, 2.5, 10000, 2000000))

#===================Sort the array===================================
def sort_by_length(arr):
    lst2 = sorted(arr, key=len)
    print(arr)
    return lst2

# arr = ["Telescopes", "Glasses", "Eyes", "Monocles"]
# sort_by_length(arr)

#================revesrs word like this ilA menahG====================
def reverse_words(text):
    return ' '.join(s[::-1] for s in text.split(' '))
text = "Ali Ghanem"
# print(reverse_words(text))

#===============Sum of two lowest positive integers===================
def sum_two_smallest_numbers(numbers):
    n = sorted(numbers)
    return sum(n[:2])
# print(sum_two_smallest_numbers([25, 42, 4, 18, 8]))

#===============Printer Errors print letter in virtucal way===========
def printer_error(s):
    denominator_ = len(s)
    errors = 0
    good_letters='abcdefghijklm'
    for i in s:
        print(i)
        if i not in good_letters:
            errors += 1
    return str(errors) + "/" + str(denominator_)
# printer_error('Hallow')

#=================Convert the binery system to dicmiale system====================================
# One To Zero Given an array of ones and zeroes, convert the equivalent binary value to an integer.
def binary_array_to_number(arr):
    return int(''.join([str(item) for item in arr]), 2)
arr = [0, 0, 0, 1,0,1,0,0,0,0,0,1,1,1,0,1,0]
# print(binary_array_to_number(arr))

#================Sum of a sequence====================
def sequence_sum(begin_number, end_number, step):
    return sum([i for i in range(begin_number, end_number+1, step)])
# print(sequence_sum(1,6,1))

#=================Find the middle element==============
def gimme(input_array):
    sorted_list = sorted(input_array)
    return input_array.index(sorted_list[1])

# liss = ['Hi','Mi','Do','Ky','Sy']
# print(gimme(liss))

#====================Nmae elemet with his index in array=================
#Write a function which takes a list of strings and returns each line prepended by the correct number.
def number(lines):
    count = 1
    line = []
    for x in lines:
        line.append(str(count) + ': ' + x)
        count += 1
    return line
# liss = ['Hi','Mi','Do','Ky','Sy']
# print(number(liss))

#====================Mine amd Max from list===========
def min_max(lst):
    return [min(lst), max(lst)]
# liss = [1,2,4,55,321,54,321,3125,656]
# print(min_max(liss))

#===================Friend or Foe?===================
def friend(x):
    return [n for n in x if len(n) == 4]
# list2 = ['231','dwqe','gfd','dsa','nbvn']
# print(friend(list2))

#====================find element in array============
def find(n):
    return sum(i for  i in range(n+1) if i % 3 == 0 or i % 5 == 0)
# print(find(10))

#=====================List Filtering int value=================
def filter_list(l):
    return [i for i in l if type(i) != str]
# list2 = [3,'nbvn',321]
# print(filter_list(list2))

#======================Find the next perfect square!============
import math
def find_next_square(sq):
    root = sq ** 0.5
    if root.is_integer():
        return (root + 1)**2
    return -1
# print(find_next_square(121))

#===============Maximum Length Difference===========
def mxdiflg(a1, a2):
    if a1 and a2:
        return max(
            len(max(a1, key=len)) - len(min(a2, key=len)),
            len(max(a2, key=len)) - len(min(a1, key=len)))
    return -1

a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# print(mxdiflg(a1,a2))

#=================Maiximum number of array===========
def maximum(nums):
    for item in nums:
        if item> Max:
            Max = item
        print (Max)
        return Max
# nums = [1,5,8,77,24,95]
# print(max(nums))
# print(len(["hellow",2,4,6]))
# i = 1
# while True:
#     if i%3 == 0:
#         break
#     print(i)
#     i+=1

# ==================== Machine learning (Numby) Array=========================
from array import array
import numpy as np
import sys as sys
import time

#====================== Create Array===============================
elment = 150000
my_list = [1,2,3,4,5,6,7]
my_array = np.array(my_list)

# print(my_list)
# print(my_array)

#print("#" * 50)

#====================== Accese to Elemnt============================
# print(my_list[3])
# print(my_array[5])
# print("#" * 50)

#====================== Performance and storeg======================
my_list1 = range(elment)
my_list2 = range(elment)
my_array1 = np.arange(elment)
my_array2 = np.arange(elment)
# print(my_array1)

#====================== For loop on the list=========================
list_start = time.time()
list_result = [(n1 +n2) for n1,n2 in zip(my_list1,my_list2)]
# print(list_result)

print("#" * 50)
# Timeing to make data list
print(f"List Time: {time.time() - list_start}")
# # Storge list
print(f"List Storge {sys.getsizeof(1) * len(list_result)}")

#==================== For in array=================================
array_statr = time.time()
array_result = my_array1 + my_array2
# print(array_result)
print("#" * 50)
# Timeing to make data array
print(f"Array Time:{time.time() - array_statr}")
# Storge Array
print(f"Array Storge {array_result.itemsize * array_result.size}")

# Slicing => [Start:End:Steps] and Indexing 
# a2 = np.array(["A","B","C","D","F"])
# print(a2.ndim)
# print(a2.shape)
# print(a2[0:5]) 

#==================== Tow Dimisonla array=================================
a2 = np.array([["A","B","S"],["C","D","F"], ["H","W","G"],["T","U","I"]])
print(a2.shape)
print(a2[2,2])
print(a2[:3,:3:2])

# Data Type and Contorl Array