'''
质解因数，比如输入90,90=2*3*3*5
'''
n = int(input("Enter a number: "))
print(n,"=",end='')
i = 2
while n != 1:
    while n%i == 0:
        n //= i
        if n == 1:
            print('{:d}'.format(i))
        else:
            print('{:d}*'.format(i),end='')
    i += 1