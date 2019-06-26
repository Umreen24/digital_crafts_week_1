original_word = input("Enter word here: ")

backwards = ""

for index in range(len(original_word)-1, -1, -1):
    backwards += original_word[index]

if backwards == original_word:
    print("PALINDROME")
else:
    print("NOT PALINDROME")










# 1 take input 
# 2 reverse input # reverse function does exist, but do not use
# c|a|t 
# range(0, len(word))
# range(len(word)-1, __, -1)
# 3 compare reverse input with actual input