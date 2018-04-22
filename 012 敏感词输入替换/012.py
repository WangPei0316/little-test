with open('filtered_words.txt') as f:
    r = f.read().split('\n')
input_word = input("请输入文本：")

wrong_words = []

for i in r:
    if i in input_word:
        wrong_words.append(i)

if wrong_words:
    for i in range(len(wrong_words)):
        input_word = input_word.replace(wrong_words[i],'*'*len(wrong_words[i]))
    print(input_word)
else:
    print(input_word)

