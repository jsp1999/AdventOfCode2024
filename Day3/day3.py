import re
from functools import reduce

text = ""
pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
patternDo = r"don\'t\(\).*?do\(\)"

with open('data.txt', 'r') as file:
    text = file.read()

cleaned_text = re.sub(patternDo, '', text, flags=re.DOTALL)

multis = [(int(x), int(y)) for x, y in re.findall(pattern, cleaned_text)]
result = reduce(lambda acc, pair: acc + pair[0] * pair[1], multis, 0)

print(result)
