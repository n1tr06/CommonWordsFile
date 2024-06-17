import re
import sys 

file_path = r'C:\Users\eitan\Desktop\Moadon\Git Repositories\CommonWordsFile\test.txt'

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
        words_dict[words[i]] = 1

for i in range(int(sys.argv[1])):
    max_key = max(words_dict, key=lambda k: words_dict[k])
    print(f"{(i+1)}. {max_key} {words_dict[max_key]} times")
    words_dict[max_key] = 0