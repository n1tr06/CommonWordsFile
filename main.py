import re

file_path = 'test.txt'

with open(file_path, 'r') as file:
    file_content = file.read()

pattern = r'[^a-zA-Z\s]'
clean_text = re.sub(pattern , '', file_content)


    





