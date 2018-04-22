import glob

codefiles = glob.glob('/home/wangpei/PycharmProjects/littletest/*.py')
code_lines = 0
code_blank_line = 0
code_comment_line = 0

for file in codefiles:
    r = open(file)
    for line in r:
        code_lines += 1
        if line.strip() == '':
            code_blank_line += 1
        elif line.strip().startswith('#'):
            code_comment_line += 1
    r.close()

print('文件数量一共{}个'.format(len(codefiles)))
print('总行数{}行'.format(code_lines))
print('空行数{}行'.format(code_blank_line))
print('注释行数{}行'.format(code_comment_line))
