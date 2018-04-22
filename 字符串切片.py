f = open('scores.txt')
lines = f.readlines()
f.close()
results = []
for line in lines:
    data = line.split()
    sum = 0
    for score in data[1:]:
        sum += int(score)
    result = '{}:{}'.format(data[0], sum)
    results.append(result)
print(results)
