# Regex
import re

# Import Tkinter for later GUI implementation
try:
  from Tkinter import *
except ImportError:
  from tkinter import *

# Scrabble Scores
scores = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}


# Scrabble words in file: sowpods.txt
valid_words = open('sowpods.txt', 'r')
list_of_words = []
for line in valid_words:
  if line.strip():
    list_of_words.append(line.strip())
valid_words.close()

# Get the rack from the command line args
rack = sys.argv[1]
# Make them lowercase
rack = rack.upper()

possible_words = []
check = True

# Check what words the letters can make and add to list of possible words
for word in list_of_words:
  newRack = rack
  check = True
  for char in word:
    index = newRack.find(char)
    if index!=-1:
      newRack = newRack.replace(newRack[index], '', 1)
    else:
      check = False
      break

  # If all letter in the word exist in the rack, add to list
  if check == True:
    possible_words.append(word)

# Now check the scores of each of the words in 'possible_words' list
word_scores = []
for word in possible_words:
  sum = 0
  for char in word:
    sum+=scores[char.lower()]
  word_scores.append(sum)


# Sort by score
# Must put in two new lists since there is no association
# between score and word right now, just index
word_list = []
score_list = []
while possible_words:
  highest_score = max(word_scores)
  index_of_score = word_scores.index(highest_score)
  word_list.append(possible_words[index_of_score])
  del possible_words[index_of_score]
  score_list.append(word_scores[index_of_score])
  del word_scores[index_of_score]

# Print out the words with their scores
print "----------------------------------------"
print "Score | Word "
print "----------------------------------------"
for index in range(len(word_list)):
  print score_list[index],"\t",word_list[index]






