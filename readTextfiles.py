# #Create a Python script that reads a text file into a list and then converts the list back into a string which is the entire file content.
# with open('sample.txt', 'r') as f:
# 	# reading the file in a list
# 	content = f.read().splitlines()
# 	# concatenating the list back into a string
# 	my_str = '\n'.join(content)
# 	print(my_str)
#
# #Create a Python function called tail that reads the last n lines of a text file.
# def tail(file, n):
# 	with open(file, 'r') as f:
# 		# reading the file in a list
# 		content = f.read().splitlines()
# 		# getting the last n elements of the list
# 		last = content[len(content)-n:]
# 		# print(last)
# 	        # concateneting the list back into a string
# 		my_str = '\n'.join(last)
# 		return my_str
#
# t = tail('sample.txt', 3)
# print(t)
#
# #Change the solution from the previous challenge so that the script that prints out the last n lines of the file refreshes the output every 3 seconds (as the file changes or updates)
# import time
# def tail(file, n):
#         with open(file, 'r') as f:
#                 # reading the file in a list
#                 content = f.read().splitlines()
#                 # getting the last n elements of the list
#                 last = content[len(content)-n:]
#                 # print(last)
#                 # concateneting the list back into a string
#                 my_str = '\n'.join(last)
#                 return my_str
#
# while True:
# 	t = tail('sample.txt', 3)
# 	print(t)
# 	time.sleep(3)
# 	print('')
#
# #Write a Python program to count the number of lines, words and characters in a text file.
# def wc(file):
# 	with open(file, 'r') as f:
# 		content = f.read().splitlines()
# 		lines = len(content)
# 		words = 0
# 		for line in content:
# 			words += len(line.split())
#
# 		chars = 0
# 		for line in content:
# 			chars += len(list(line))
#
# 		return lines, words, chars
#
#
# print(wc('sample.txt'))

#Write a Python program that calculates the net amount of a bank account based on the transactions saved in a text file.
# with open('banking.txt', 'r') as f:
# 	content = f.read().splitlines()
#
# 	deposit, withdrawal = 0, 0
#
# 	for item in content:
# 		tmp = item.split(':')
# # print(tmp) # -> ['D', '300']
# 		if tmp[0] == 'D':
# 			deposit += int(tmp[1])
# 		elif tmp[0] == 'W':
# 			withdrawal += int(tmp[1])
# 		else:
# 			print('File format error')
#
# balance = deposit - withdrawal
# print(balance)

#Write a Python script that compares two text files line by line and display the lines that differ.

# with open('a.txt') as f:
#     file1 = f.read().splitlines()
#
# with open('b.txt') as f:
#     file2 = f.read().splitlines()
#
# file = list(zip(file1, file2))
# i = 0
# for item in file:
#     i += 1
#     if item[0] != item [1]:
#         print(f'file1 ({i}): {item[0]}, file2 ({i}): {item[1]}')

#Write a Python script that reads the file in a dictionary.
# The words in the file will be the dictionary keys and the length of each word the corresponding values.

# with open('american-english.txt') as f:
#     words = f.read().splitlines()
#
#     words_and_length = dict()
#     for w in words:
#         words_and_length[w] = len(w)
#
#     for k, v in words_and_length.items():
#         print(f'{k} -> {v}')

# Write a Python script that finds the first 100 longest words in a file.
# with open('american-english.txt') as f:
#     words = f.read().splitlines()
#
#     words_and_length = dict()
#     for w in words:
#         words_and_length[w] = len(w)
#     #print(words_and_length)
#
#     words_list = sorted(words_and_length.items(), key=lambda x:x[1], reverse=True)
#     print(words_list[:100])

#Write a Python script that finds the number of occurrences of each letter of the alphabet in all the words in the dictionary.

import string
letters = dict()

# initializing the dictionary with all letters as keys and zero as values
for c in string.ascii_lowercase:
     letters[c] = 0
#print(letters)

with open('american-english.txt', 'r') as words:
    for w in words:
        for char in string.ascii_lowercase:
            letters[char] += w.count(char)

#print(letters)
#find the 3 most frequently used letters in all English Words.
print(sorted(letters.items(), key=lambda x:x[1], reverse=True))