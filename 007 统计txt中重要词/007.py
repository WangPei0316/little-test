import glob, os,re
from string import punctuation
from collections import Counter


def key_words():
    for file in glob.glob('/home/wangpei/PycharmProjects/littletest/007 统计txt中重要词/articles/*.txt'):
        filepath, filename = os.path.split(file)
        r = open(file)
        words = r.read()
        r.close()
        new_words = re.sub(r'[{}]+'.format(punctuation), '', words).strip().lower()
        pure_words = re.split(r'[;,.:\'\n\"”\s]+', new_words)
        print(Counter(pure_words).most_common(1))

key_words()
