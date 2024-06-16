import re

file_path = 'test.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

pattern = r'[^a-zA-Z\s]'
clean_text = re.sub(pattern , ' ', file_content)

words = clean_text.split()

print(words)
words_dict = {}
for i in range(len(words)):
    if words[i] in words_dict:
        words_dict[words[i]] += 1
    else:
        words_dict[words[i]] = 0


print (words_dict)







