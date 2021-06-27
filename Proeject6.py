import matplotlib.pyplot as plt
from collections import Counter
import random
import time
from bisect import bisect_right


# A - takes a list as a parameter and returns True if the list is sorted in ascending order and False otherwise
def is_sorted(list):

  for i in range(1, len(list)):  #for loop iterates over elements of the list
    if list[i - 1] > list[i]:  #if elements are not in ascending order, returns False
      return False
  return True

# B - takes two strings and returns True if they are anagrams.
def is_anagram(str1, str2):
  # Get lengths of both strings
  x1 = len(str1)
  x2 = len(str2)

  # If length of both strings is not same, they cannot be anagram

  if x1 != x2:
    return -1

  # Both strings are sorted
  str1 = sorted(str1)
  str2 = sorted(str2)

  # Comparing sorted strings
  for i in range(0, x1):
    if str1[i] != str2[i]:
      return 0

  return -1

# C - takes a list and returns True if there is any element that appears more than once. Generates random birthdays
# to prove birthday paradox
def has_duplicates(list):
  x = 0    #initializing variables
  y = 0
  for x in range(0, len(list)): #accessing each element of the list
    count = 1
    for y in range(0, len(list)):  #accessing each element of the list
      if x == y: #if elements are equal, we continue
        continue
      if list[x] == list[y]:  #if there is a repeated element, we add it to count
        count += 1
    if count > 1:
      return True
  return False      #otherwise, function returns false

def birthday_probability(people):
  tries = 2000  #generating amount of tries for more precision
  duplicates = 0  #initializing duplicates count
  for tries in range(int(tries)):      #for loops iterates over each try
    days = [0] * 366  #initializing number of days in a year
    for _ in range(people):
      birthday_random = random.randint(1, 365)   #we generate random birthdays
      days[birthday_random] += 1
      if days[birthday_random] == 2: #if there are two of the same birthdays, we add them to duplicates
        duplicates += 1
        break
  return duplicates / tries   #function returns probability of 2 people having the same birthday


# D - that takes a list and returns a new list with only the unique elements from the original

def remove_duplicates(list):

  final_list = []

  for element in list:   #iteration over each element in the list
    if element not in final_list:
      final_list.append(element)   #adding unique elements to the final list
  return final_list


# E - reads the file words.txt and builds a list with one element per word

def time_function1():
  #using append method
  file = "/Users/yuliiamartynenko/Downloads/words.txt"
  t0 = time.time()
  word_list = []

  with open(file) as f:
    for line in f:
      line = line.split()
      for word in line:
        word_list.append(word)
    print(word_list)

  t1 = time.time() - t0
  print("Time elapsed: ", t1)

def time_function2():
  # using the idiom t = t + [x]
  file = "/Users/yuliiamartynenko/Downloads/words.txt"
  t0 = time.time()
  word_list = []

  with open(file) as f:
    for line in f:
      for word in line.split():
        word_list = word_list + [word]
    print(word_list)

  t1 = time.time() - t0
  print("Time elapsed: ", t1)


#F -  takes a sorted list and a target value and returns the index of the value in the list, if it’s there, or
# None if it’s not.

def bisect(sorted_list, bottom, top, target_value):
  if top >= bottom:
    middle = (top + bottom) // 2
    # If element is present at the middle itself

    if sorted_list[middle] == target_value:
      return middle

    # If element is smaller than middle, then it can only be in left part of the list
    elif sorted_list[middle] > target_value:
      return bisect(sorted_list, bottom, middle - 1, target_value)
    # Else the element can only be in the right part of the list
    else:
      return bisect(sorted_list, middle + 1, top, target_value)
  else:
    # Element is not present in the list
    return None


  # G - counts the number of times each unique letter (character) occurs in a sentence entered by the user
# plus, histogram
def frequency_counter(test_str):
  final_freq = {}

  for letter in test_str:
    letter = letter.lower()
    if letter != "" and letter != " ":
      if letter in final_freq:
        final_freq[letter] += 1
      else:
        final_freq[letter] = 1

  for key, value in final_freq.items():
    print(key, ':', value)

  dictionary = final_freq
  plt.bar(sorted(list(dictionary.keys())), dictionary.values(), color='skyblue')
  plt.show()

# H - moby.txt file operations
# 1) count number of words in the file
def counting_words():

  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"
  words_count = 0

  with open(fname, 'r') as f:
    for line in f.readlines():
      words = line.split()
      words_count += len(words)
  return words_count

# 2) frequency of each letter in the file
def counting_letters():

  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"
  validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  with open(fname) as f:
    c = Counter()
    for line in f.readlines():
      for char in line:
        if char in validLetters:
          c += Counter(char)
    return c

# 3) frequency of uppercase letters in the file
def counting_uppercase():
  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"
  with open(fname) as f:
    c = Counter()
    for line in f.readlines():
      for char in line:
        if char.istitle():
          c += Counter(char)
    return c

# 4) frequency of lowercase letters in the file
def counting_lowercase():
  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"
  with open(fname) as f:
    c = Counter()
    for line in f.readlines():
      for char in line:
        if char.islower():
          c += Counter(char)
    return c
# # 5)Convert all uppercase to lower case and vise versa, write in a new file.
def converting_letters():
  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"

  with open(fname) as s:
    new_str = ""
    for line in s.readlines():
      for char in line:
        if char.istitle():
          new_str += char.lower()
        elif char.islower():
          new_str += char.upper()
        else:
          new_str += char

    return new_str

def creating_output_file_upper_to_lower():

  new_file = open("converting_letters.txt", "wt")
  new_file.write(converting_letters() + '\n')
  new_file.close()

# 6)
def creating_output_file():

  out_file = open("output.txt", "w")

  out_file.writelines("File's total word Counter ")
  out_file.writelines(str(counting_words()) + '\n')

  out_file.writelines("The letter ")
  out_file.writelines(str(counting_letters()) + '\n')

  out_file.writelines("The uppercase letter ")
  out_file.writelines(str(counting_uppercase()) + '\n')

  out_file.writelines("The lowercase letter ")
  out_file.writelines(str(counting_lowercase()) + '\n')

  out_file.close()

# 7) plotting letter frequency
def plotting_histogram():

  fname = "/Users/yuliiamartynenko/Downloads/moby.txt"
  validLetters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

  with open(fname) as f:
    c = Counter()
    for line in f.readlines():
      for char in line.lower():
        if char in validLetters:
          c += Counter(char)

    dictionary = c
    plt.bar(sorted(list(dictionary.keys())), dictionary.values(), color="skyblue")
    plt.show()



if __name__ == '__main__':
# A)
  sorted = print(is_sorted(['b', 'a', 'd']))
  sorted1 = print(is_sorted([1, 2, 3, 4, 5]))

B)
  str1 = "test"
  str2 = "ttew"
  str3 = "tset"

  if is_anagram(str1, str2):
    print("True")
  else:
    print("False")

  if is_anagram(str1, str3):
    print("True")
  else:
    print("False")

# C)
  list = [1, 2, 3]
  list1 = [1, 3, 3]
  print(has_duplicates(list))
  print(has_duplicates(list1))

  people = 23
  p = birthday_probability(people)
  print("The chances that two of {} people have the same birthday are {:.0%}.".format(people, p))
#
# D)
  list = [1, 2, 3]
  list1 = [1, 3, 3]
  print(remove_duplicates(list))
  print(remove_duplicates(list1))
#
# E)
  time_function1()
  time_function2()
# For every iteration, there will have to be the same amount of elements copied from the original list to form a new list.

# # F)
  sorted_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # test1
  target_value = 'd'
  result = bisect(sorted_list, 0, len(sorted_list) - 1, target_value)

  sorted_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']  # test1
  target_value1 = 'k'
  result1 = bisect(sorted_list, 0, len(sorted_list) - 1, target_value1)

  if result != None:
    print("Element is located at index", str(result))
  else:
    print("None")

  if result1 != None:
    print("Element is located at index", str(result))
  else:
    print("None")

# G)
  frequency_counter(test_str=input("Please, enter a string "))

# H)
# 1)
  counting_words()
# 2)
  counting_letters()
# 3)
  counting_uppercase()
# 4)
  counting_lowercase()
# 5)
  converting_letters()
  creating_output_file_upper_to_lower()

# 6)
  creating_output_file()
# 7)
  plotting_histogram()

