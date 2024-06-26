import re
import sys 

file_path = r'test.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

pattern = r'[^a-zA-Z\s]'
clean_text = re.sub(pattern , ' ', file_content)

words = clean_text.split()

words_dict = {}
for i in range(len(words)):
    if words[i] in words_dict:
        words_dict[words[i]] += 1
    else:
        words_dict[words[i]] = 1

n = int(sys.argv[1])
if n > len(words):
    n = len(words)

for i in range(n):
    max_key = max(words_dict, key=lambda k: words_dict[k])
    print(f"{(i+1)}. \"{max_key}\" {words_dict[max_key]} times")
    words_dict[max_key] = 0