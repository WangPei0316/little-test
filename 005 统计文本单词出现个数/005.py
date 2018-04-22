import re
from string import punctuation
from collections import Counter

r = open('test.txt')
words = r.read()
r.close()

new_words = re.sub(r'[{}]+'.format(punctuation), '', words).strip().lower()
pure_words = re.split(r'[;,.:\'\n\"”\s]+', new_words)

print(Counter(pure_words))
